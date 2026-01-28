#!/usr/bin/env python3
"""Script to add descriptions and checklists to Trello cards."""
import urllib.request
import urllib.parse
import json
import os

# Use environment variables for credentials
KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")

CARDS = {
    "697a01541ceaa66f8bbe39a3": {
        "desc": """## PROD-01: Sprint Planning Dashboard

### User Story
**As a** Scrum Master,
**I want** a comprehensive sprint planning dashboard
**So that** I can effectively plan, visualize, and communicate sprint objectives to my team.

**Story Points**: 8 | **Priority**: High | **Epic**: Operations Hub Core

### Technical Context
| Aspect | Details |
|--------|--------|
| Component | Dashboard Module |
| Dependencies | Velocity Tracker API, Backlog Manager |
| UI Framework | React with Material UI M3 |
| API Layer | Laravel REST endpoints |

### Risk Summary
- Complex data aggregation → Redis caching
- Race conditions → Optimistic locking
- UI complexity → Usability testing""",
        "checklist": [
            "Dashboard displays current sprint info (name, dates, goals)",
            "Sprint backlog items visible with status indicators",
            "Team capacity calculated and displayed",
            "Burndown chart updates in real-time",
            "Sprint goals editable by authorized users",
            "Unit tests achieve 80% coverage",
            "Integration tests pass",
            "WCAG 2.1 AA accessibility audit passes",
            "Code review completed",
            "Documentation updated"
        ]
    },
    "697a01635ec3365d52cc0490": {
        "desc": """## PROD-02: Backlog Management System

### User Story
**As a** Product Owner,
**I want** a robust backlog management system
**So that** I can prioritize, refine, and organize product backlog items efficiently.

**Story Points**: 13 | **Priority**: High | **Epic**: Backlog Operations

### Technical Context
| Aspect | Details |
|--------|--------|
| Component | Backlog Manager Module |
| UI | React with drag-and-drop (react-beautiful-dnd) |
| API | Laravel REST with pagination |
| Features | Version history, Markdown support, Export to CSV/JSON |

### Risk Summary
- Large backlog performance → Virtualized lists
- Concurrent edits → WebSocket notifications
- Slow queries → Database indexing""",
        "checklist": [
            "CRUD operations functional for backlog items",
            "Drag-and-drop reordering persists to database",
            "Filtering by status, assignee, sprint, tags",
            "Search returns results within 200ms",
            "Bulk operations handle 50 items",
            "Version history shows last 20 changes",
            "Export to CSV and JSON",
            "Markdown renders correctly",
            "Mobile touch reordering works",
            "Page load < 2 seconds with 500 items",
            "Product Owner sign-off"
        ]
    },
    "697a0165e8f174bfdb0383a0": {
        "desc": """## PROD-03: Team Velocity Tracker

### User Story
**As a** Scrum Master,
**I want** a velocity tracking system with historical analysis
**So that** I can accurately forecast team capacity and identify improvement trends.

**Story Points**: 8 | **Priority**: Medium | **Epic**: Analytics & Reporting

### Technical Context
| Aspect | Details |
|--------|--------|
| Component | Velocity Analytics Module |
| Visualization | Chart.js |
| API | Laravel with aggregation endpoints |
| Features | 12+ sprint history, trend analysis, forecasting |

### Risk Summary
- Story point inflation → Calibration tools
- Privacy concerns → Opt-in individual tracking
- Missing data → Graceful handling""",
        "checklist": [
            "Velocity calculated from sprint completion data",
            "Historical chart shows last 12 sprints",
            "3-sprint moving average trend line",
            "Individual velocity opt-in available",
            "Forecast predictions within 10% accuracy",
            "PDF report export",
            "Dashboard widget for current progress",
            "Velocity threshold notifications",
            "Chart renders in < 1 second",
            "Formula documentation complete"
        ]
    },
    "697a0166e721a1638bfd12a2": {
        "desc": """## PROD-04: Risk Assessment Module

### User Story
**As a** Project Manager,
**I want** an integrated risk assessment module
**So that** I can identify, track, and mitigate project risks proactively.

**Story Points**: 13 | **Priority**: Medium | **Epic**: Risk & Governance

### Technical Context
| Aspect | Details |
|--------|--------|
| Component | Risk Management Module |
| UI | React with interactive risk matrix |
| API | Laravel with risk scoring algorithms |
| Features | Automated detection, notification system |

### Risk Summary
- Administrative burden → Streamlined UI
- Scoring inconsistency → Calibration examples
- Alert fatigue → Configurable thresholds""",
        "checklist": [
            "Risk matrix displays all active risks",
            "Risk creation with probability/impact (1-5)",
            "Mitigation actions linked with status tracking",
            "Auto risk score calculation",
            "Color coding (green/yellow/red)",
            "Risk-adjusted sprint capacity",
            "Automated high-severity alerts",
            "Risk history and audit trail",
            "Excel export for risk register",
            "Mobile responsive",
            "Security review completed"
        ]
    },
    "697a0168d961918299aeeaf6": {
        "desc": """## PROD-05: Operations Hub Integration

### User Story
**As a** Team Lead,
**I want** a unified operations hub
**So that** I can access all project management tools from a single dashboard.

**Story Points**: 21 | **Priority**: High | **Epic**: Platform Integration

### Technical Context
| Aspect | Details |
|--------|--------|
| Component | Operations Hub Core |
| Dependencies | PROD-01 to PROD-04 |
| UI | React with modular widget system |
| API | Laravel with unified GraphQL gateway |
| Features | Customizable dashboard, SSO, activity feed |

### Risk Summary
- Integration complexity → Modular architecture
- Performance degradation → Lazy loading
- Information density → Progressive disclosure""",
        "checklist": [
            "Dashboard loads with default widgets",
            "Widget placement customizable and saved",
            "All modules (PROD-01 to PROD-04) as widgets",
            "Notification center aggregates all alerts",
            "Quick actions execute in-place",
            "Activity feed shows last 50 actions",
            "Preferences persist across sessions",
            "State syncs across browser tabs",
            "Initial load < 3 seconds",
            "Widget lazy loading implemented",
            "Responsive on all viewports",
            "Keyboard navigation accessible",
            "E2E tests cover critical journeys",
            "Deployment documentation complete"
        ]
    }
}

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

def update_card_description(card_id, desc):
    """Update card description."""
    url = f"https://api.trello.com/1/cards/{card_id}"
    data = {"key": KEY, "token": TOKEN, "desc": desc}
    result = make_request(url, data, "PUT")
    if result:
        print(f"✅ Updated description for card {card_id}")
    return result

def create_checklist(card_id, items):
    """Create checklist with items."""
    # Create checklist
    url = f"https://api.trello.com/1/checklists"
    data = {"key": KEY, "token": TOKEN, "idCard": card_id, "name": "Acceptance Criteria"}
    result = make_request(url, data, "POST")
    
    if not result:
        print(f"❌ Failed to create checklist for {card_id}")
        return
    
    checklist_id = result["id"]
    print(f"✅ Created checklist {checklist_id}")
    
    # Add items
    for item in items:
        url = f"https://api.trello.com/1/checklists/{checklist_id}/checkItems"
        data = {"key": KEY, "token": TOKEN, "name": item}
        make_request(url, data, "POST")
    
    print(f"   Added {len(items)} items to checklist")

def main():
    """Main execution."""
    print("=" * 50)
    print("NexusFlow Trello Card Configuration")
    print("=" * 50)
    
    for card_id, config in CARDS.items():
        print(f"\n📋 Processing card: {card_id}")
        update_card_description(card_id, config["desc"])
        create_checklist(card_id, config["checklist"])
    
    print("\n" + "=" * 50)
    print("✅ All cards configured successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
