#!/usr/bin/env python3
"""Script to setup Sprint 01 workflow dynamics in Trello."""
import urllib.request
import urllib.parse
import json
import os
from datetime import datetime, timedelta

# Environment variables for credentials
KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")

# List IDs
BACKLOG_LIST = "697a012c98a9422774047b29"
SPRINT_PLANNING_LIST = "697a012e9253cee4e94c3f4d"
IN_PROGRESS_LIST = "697a013035915f63623c77dd"
BLOCKERS_LIST = "697a0132e76d2c686166a044"

# Due date: 7 days from now
DUE_DATE = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%dT17:00:00.000Z")

def make_request(url, data=None, method="GET"):
    """Make HTTP request to Trello API."""
    if data:
        data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_cards_from_list(list_id):
    """Get all cards from a list."""
    url = f"https://api.trello.com/1/lists/{list_id}/cards?key={KEY}&token={TOKEN}"
    return make_request(url)

def move_card(card_id, list_id):
    """Move card to a different list."""
    url = f"https://api.trello.com/1/cards/{card_id}"
    data = {"key": KEY, "token": TOKEN, "idList": list_id}
    return make_request(url, data, "PUT")

def set_due_date(card_id, due_date):
    """Set due date on card."""
    url = f"https://api.trello.com/1/cards/{card_id}"
    data = {"key": KEY, "token": TOKEN, "due": due_date}
    return make_request(url, data, "PUT")

def add_member(card_id, member_id):
    """Add member to card."""
    url = f"https://api.trello.com/1/cards/{card_id}/idMembers"
    data = {"key": KEY, "token": TOKEN, "value": member_id}
    return make_request(url, data, "POST")

def add_comment(card_id, text):
    """Add comment to card."""
    url = f"https://api.trello.com/1/cards/{card_id}/actions/comments"
    data = {"key": KEY, "token": TOKEN, "text": text}
    return make_request(url, data, "POST")

def get_checklists(card_id):
    """Get checklists from card."""
    url = f"https://api.trello.com/1/cards/{card_id}/checklists?key={KEY}&token={TOKEN}"
    return make_request(url)

def complete_checklist_item(card_id, checklist_id, item_id):
    """Mark checklist item as complete."""
    url = f"https://api.trello.com/1/cards/{card_id}/checkItem/{item_id}"
    data = {"key": KEY, "token": TOKEN, "state": "complete"}
    return make_request(url, data, "PUT")

def get_board_members():
    """Get board members."""
    url = f"https://api.trello.com/1/boards/kJmHUUVR/members?key={KEY}&token={TOKEN}"
    return make_request(url)

def main():
    """Main execution."""
    if not KEY or not TOKEN:
        print("Error: TRELLO_KEY and TRELLO_TOKEN must be set")
        return
    
    print("=" * 60)
    print("NexusFlow - Sprint 01 Workflow Setup")
    print("=" * 60)
    
    # Get all cards from backlog
    print("\n📋 Getting cards from PRODUCT BACKLOG...")
    cards = get_cards_from_list(BACKLOG_LIST)
    if not cards:
        print("   ❌ Failed to get cards")
        return
    
    # Find the 4 target cards
    target_cards = {}
    for card in cards:
        name = card["name"]
        if name.startswith("PROD-01:"):
            target_cards["PROD-01"] = card
        elif name.startswith("LOG-01:"):
            target_cards["LOG-01"] = card
        elif name.startswith("COM-01:"):
            target_cards["COM-01"] = card
        elif name.startswith("FAC-01:"):
            target_cards["FAC-01"] = card
    
    print(f"   ✅ Found {len(target_cards)} target cards")
    for key, card in target_cards.items():
        print(f"      - {key}: {card['id']}")
    
    # Get board member (Manu)
    print("\n👤 Getting board members...")
    members = get_board_members()
    member_id = None
    if members:
        for m in members:
            print(f"   - {m['fullName']} ({m['id']})")
            member_id = m["id"]  # Use first/only member
    
    # === PHASE 1: Move to Sprint Planning ===
    print("\n" + "=" * 60)
    print("Phase 1: Sprint Planning")
    print("=" * 60)
    
    for key in ["PROD-01", "LOG-01", "COM-01", "FAC-01"]:
        if key not in target_cards:
            print(f"   ❌ {key} not found")
            continue
        
        card = target_cards[key]
        card_id = card["id"]
        
        print(f"\n📋 Processing {key}...")
        
        # Move to Sprint Planning
        move_card(card_id, SPRINT_PLANNING_LIST)
        print(f"   ✅ Moved to SPRINT PLANNING")
        
        # Set due date
        set_due_date(card_id, DUE_DATE)
        print(f"   ✅ Due date set: 2026-02-04")
        
        # Add member
        if member_id:
            add_member(card_id, member_id)
            print(f"   ✅ Member assigned")
    
    # === PHASE 2: Kanban Flow ===
    print("\n" + "=" * 60)
    print("Phase 2: Kanban Flow (IN PROGRESS)")
    print("=" * 60)
    
    # Move PROD-01 to IN PROGRESS
    if "PROD-01" in target_cards:
        card_id = target_cards["PROD-01"]["id"]
        
        move_card(card_id, IN_PROGRESS_LIST)
        print(f"\n📋 PROD-01 moved to IN PROGRESS")
        
        # Mark first 3 checklist items as complete
        checklists = get_checklists(card_id)
        if checklists:
            checklist = checklists[0]
            checklist_id = checklist["id"]
            items = checklist.get("checkItems", [])
            
            for i, item in enumerate(items[:3]):
                complete_checklist_item(card_id, checklist_id, item["id"])
                print(f"   ✅ Checked item {i+1}: {item['name'][:40]}...")
        
        # Add comment
        comment = "🚀 Starting execution phase. Initial setup complete.\n\n---\n\n🚀 Iniciando fase de ejecución. Configuración inicial completada."
        add_comment(card_id, comment)
        print(f"   ✅ Comment added")
    
    # Move COM-01 to IN PROGRESS
    if "COM-01" in target_cards:
        card_id = target_cards["COM-01"]["id"]
        move_card(card_id, IN_PROGRESS_LIST)
        print(f"\n📋 COM-01 moved to IN PROGRESS")
    
    # === PHASE 3: Impediment Management ===
    print("\n" + "=" * 60)
    print("Phase 3: Impediment Management (BLOCKERS)")
    print("=" * 60)
    
    if "LOG-01" in target_cards:
        card_id = target_cards["LOG-01"]["id"]
        
        move_card(card_id, BLOCKERS_LIST)
        print(f"\n📋 LOG-01 moved to BLOCKERS")
        
        # Add risk comment
        risk_comment = "⚠️ **RISK / RIESGO**\n\nDependency detected: Waiting for API credentials from third-party provider. ETA: 48 hours.\n\nMitigation: Proceeding with mock data for development while awaiting production credentials.\n\n---\n\n⚠️ **RIESGO**\n\nDependencia detectada: Esperando credenciales API de proveedor externo. ETA: 48 horas.\n\nMitigación: Continuando con datos mock para desarrollo mientras esperamos credenciales de producción."
        add_comment(card_id, risk_comment)
        print(f"   ✅ Risk comment added")
    
    print("\n" + "=" * 60)
    print("✅ Sprint 01 workflow setup complete!")
    print("=" * 60)
    print(f"\nSummary:")
    print(f"  - SPRINT PLANNING: FAC-01")
    print(f"  - IN PROGRESS: PROD-01, COM-01")
    print(f"  - BLOCKERS: LOG-01")

if __name__ == "__main__":
    main()
