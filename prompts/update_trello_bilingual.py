#!/usr/bin/env python3
"""Script to update Trello cards with bilingual content."""
import urllib.request
import urllib.parse
import json
import os

# Use environment variables for credentials
KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")

# Card updates with bilingual content
CARDS = {
    "697a01541ceaa66f8bbe39a3": {
        "name": "PROD-01: Sprint Planning Dashboard / Panel de Planificación de Sprint",
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
- UI complexity → Usability testing

---

## PROD-01: Panel de Planificación de Sprint

### Historia de Usuario
**Como** Scrum Master,
**Quiero** un panel de planificación de sprint integral
**Para** poder planificar, visualizar y comunicar eficazmente los objetivos del sprint a mi equipo.

**Story Points**: 8 | **Prioridad**: Alta | **Epic**: Núcleo del Operations Hub

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Dashboard |
| Dependencias | API del Velocity Tracker, Gestor de Backlog |
| Framework UI | React con Material UI M3 |
| Capa de API | Endpoints REST con Laravel |

### Resumen de Riesgos
- Agregación compleja de datos → Caché con Redis
- Condiciones de carrera → Bloqueo optimista
- Complejidad de UI → Pruebas de usabilidad"""
    },
    "697a01635ec3365d52cc0490": {
        "name": "PROD-02: Backlog Management System / Sistema de Gestión de Backlog",
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
- Slow queries → Database indexing

---

## PROD-02: Sistema de Gestión de Backlog

### Historia de Usuario
**Como** Product Owner,
**Quiero** un sistema robusto de gestión de backlog
**Para** poder priorizar, refinar y organizar los elementos del product backlog de manera eficiente.

**Story Points**: 13 | **Prioridad**: Alta | **Epic**: Operaciones de Backlog

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo Gestor de Backlog |
| UI | React con drag-and-drop (react-beautiful-dnd) |
| API | Laravel REST con paginación |
| Características | Historial de versiones, soporte Markdown, exportación CSV/JSON |

### Resumen de Riesgos
- Rendimiento con backlogs grandes → Listas virtualizadas
- Ediciones concurrentes → Notificaciones WebSocket
- Queries lentas → Indexado de base de datos"""
    },
    "697a0165e8f174bfdb0383a0": {
        "name": "PROD-03: Team Velocity Tracker / Tracker de Velocidad del Equipo",
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
- Missing data → Graceful handling

---

## PROD-03: Tracker de Velocidad del Equipo

### Historia de Usuario
**Como** Scrum Master,
**Quiero** un sistema de seguimiento de velocidad con análisis histórico
**Para** poder pronosticar con precisión la capacidad del equipo e identificar tendencias de mejora.

**Story Points**: 8 | **Prioridad**: Media | **Epic**: Analítica y Reporting

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Analítica de Velocidad |
| Visualización | Chart.js |
| API | Laravel con endpoints de agregación |
| Características | Historial de 12+ sprints, análisis de tendencias, pronóstico |

### Resumen de Riesgos
- Inflación de story points → Herramientas de calibración
- Preocupaciones de privacidad → Tracking individual opt-in
- Datos faltantes → Manejo elegante"""
    },
    "697a0166e721a1638bfd12a2": {
        "name": "PROD-04: Risk Assessment Module / Módulo de Evaluación de Riesgos",
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
- Alert fatigue → Configurable thresholds

---

## PROD-04: Módulo de Evaluación de Riesgos

### Historia de Usuario
**Como** Project Manager,
**Quiero** un módulo integrado de evaluación de riesgos
**Para** poder identificar, rastrear y mitigar riesgos del proyecto de manera proactiva.

**Story Points**: 13 | **Prioridad**: Media | **Epic**: Riesgo y Gobernanza

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Gestión de Riesgos |
| UI | React con matriz de riesgos interactiva |
| API | Laravel con algoritmos de scoring |
| Características | Detección automatizada, sistema de notificaciones |

### Resumen de Riesgos
- Carga administrativa → UI optimizada
- Inconsistencia de scoring → Ejemplos de calibración
- Fatiga de alertas → Umbrales configurables"""
    },
    "697a0168d961918299aeeaf6": {
        "name": "PROD-05: Operations Hub Integration / Integración del Operations Hub",
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
- Information density → Progressive disclosure

---

## PROD-05: Integración del Operations Hub

### Historia de Usuario
**Como** Team Lead,
**Quiero** un operations hub unificado
**Para** poder acceder a todas las herramientas de gestión de proyectos desde un solo dashboard.

**Story Points**: 21 | **Prioridad**: Alta | **Epic**: Integración de Plataforma

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Núcleo del Operations Hub |
| Dependencias | PROD-01 a PROD-04 |
| UI | React con sistema de widgets modular |
| API | Laravel con gateway GraphQL unificado |
| Características | Dashboard personalizable, SSO, feed de actividad |

### Resumen de Riesgos
- Complejidad de integración → Arquitectura modular
- Degradación de rendimiento → Carga diferida
- Densidad de información → Divulgación progresiva"""
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

def update_card(card_id, name, desc):
    """Update card name and description."""
    url = f"https://api.trello.com/1/cards/{card_id}"
    data = {"key": KEY, "token": TOKEN, "name": name, "desc": desc}
    result = make_request(url, data, "PUT")
    if result:
        print(f"✅ Updated card: {name[:50]}...")
    return result

def main():
    """Main execution."""
    if not KEY or not TOKEN:
        print("❌ Error: TRELLO_KEY and TRELLO_TOKEN environment variables must be set")
        return
    
    print("=" * 60)
    print("NexusFlow Trello Cards - Bilingual Update")
    print("=" * 60)
    
    for card_id, config in CARDS.items():
        print(f"\n📋 Processing card: {card_id}")
        update_card(card_id, config["name"], config["desc"])
    
    print("\n" + "=" * 60)
    print("✅ All cards updated with bilingual content!")
    print("=" * 60)

if __name__ == "__main__":
    main()
