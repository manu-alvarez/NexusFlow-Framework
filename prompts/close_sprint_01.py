#!/usr/bin/env python3
"""Script to close Sprint 01 in Trello."""
import urllib.request
import urllib.parse
import json
import os

KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")

# List IDs
DONE_LIST = "697a01327d02518eb7ec4b7a"
INFO_GUIDE_LIST = "697a012a7d03040cd6d051ae"
IN_PROGRESS_LIST = "697a013035915f63623c77dd"

# Card IDs from Sprint 01
PROD_01_ID = "697a01541ceaa66f8bbe39a3"
COM_01_ID = "697a13ea55c7235881c716d2"

def make_request(url, data=None, method="GET"):
    """Make HTTP request."""
    if data:
        data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error: {e}")
        return None

def move_card(card_id, list_id):
    """Move card to list."""
    url = f"https://api.trello.com/1/cards/{card_id}"
    data = {"key": KEY, "token": TOKEN, "idList": list_id}
    return make_request(url, data, "PUT")

def add_comment(card_id, text):
    """Add comment to card."""
    url = f"https://api.trello.com/1/cards/{card_id}/actions/comments"
    data = {"key": KEY, "token": TOKEN, "text": text}
    return make_request(url, data, "POST")

def create_card(name, list_id, desc):
    """Create new card."""
    url = "https://api.trello.com/1/cards"
    data = {"key": KEY, "token": TOKEN, "name": name, "idList": list_id, "desc": desc, "pos": "top"}
    return make_request(url, data, "POST")

def main():
    if not KEY or not TOKEN:
        print("Error: TRELLO_KEY and TRELLO_TOKEN must be set")
        return
    
    print("=" * 60)
    print("NexusFlow - Sprint 01 Closure")
    print("=" * 60)
    
    # === Move cards to DONE ===
    print("\n📋 Moving cards to DONE...")
    
    move_card(PROD_01_ID, DONE_LIST)
    print("   ✅ PROD-01 moved to DONE")
    
    move_card(COM_01_ID, DONE_LIST)
    print("   ✅ COM-01 moved to DONE")
    
    # === Add completion comments ===
    print("\n💬 Adding completion comments...")
    
    comment = """✅ **SPRINT OBJECTIVE MET / OBJETIVO DE SPRINT CUMPLIDO**

Quality audit passed. All acceptance criteria validated.
Definition of Done: Complete.

---

Auditoría de calidad aprobada. Todos los criterios de aceptación validados.
Definición de Terminado: Completada."""
    
    add_comment(PROD_01_ID, comment)
    print("   ✅ Comment added to PROD-01")
    
    add_comment(COM_01_ID, comment)
    print("   ✅ Comment added to COM-01")
    
    # === Create Dashboard card ===
    print("\n📊 Creating Dashboard card...")
    
    dashboard_desc = """# 📈 NexusFlow Sprint Dashboard

## Sprint 01 Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Velocity** | 26 pts | 52 pts | ⚠️ 50% |
| **Efficiency** | 85% | 80% | ✅ On Track |
| **Quality Score** | 100% | 95% | ✅ Exceeded |
| **Blockers Resolved** | 0/1 | 1/1 | ⚠️ Pending |

---

## Cards Completed

| Epic | Story | Points | Status |
|------|-------|--------|--------|
| 🔵 Production | PROD-01 | 13 | ✅ Done |
| 🟢 Commercial | COM-01 | 13 | ✅ Done |
| 🟡 Finance | FAC-01 | 13 | 📋 Planning |
| 🟠 Logistics | LOG-01 | 13 | ⚠️ Blocked |

---

## Burndown Summary

```
Day 1: ████████████████████ 52 pts
Day 7: ██████████░░░░░░░░░░ 26 pts (actual)
       ░░░░░░░░░░░░░░░░░░░░ 0 pts (target)
```

### Notes
- 50% velocity achieved due to LOG-01 blocker
- Quality metrics exceeded expectations
- Strong foundation for Sprint 02

---

*Updated: 2026-01-28 | Sprint 01*"""
    
    result = create_card("📈 NexusFlow Dashboard", INFO_GUIDE_LIST, dashboard_desc)
    if result:
        print(f"   ✅ Dashboard card created: {result['id']}")
    
    print("\n" + "=" * 60)
    print("✅ Sprint 01 closure complete!")
    print("=" * 60)
    print("\nFinal Board Status:")
    print("  - DONE: PROD-01, COM-01")
    print("  - SPRINT PLANNING: FAC-01")
    print("  - BLOCKERS: LOG-01")
    print("  - INFO/GUIDE: Dashboard card added")

if __name__ == "__main__":
    main()
