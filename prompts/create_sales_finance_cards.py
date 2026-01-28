#!/usr/bin/env python3
"""Script to create Sales and Finance cards in Trello with bilingual content."""
import urllib.request
import urllib.parse
import json
import os

# Environment variables for credentials
KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")

# Board and list IDs
BACKLOG_LIST_ID = "697a012c98a9422774047b29"
COMERCIAL_LABEL_ID = "697a000e676a1a79e92b703b"  # Green
FACTURACION_LABEL_ID = "697a000e676a1a79e92b703c"  # Yellow

# Commercial cards
COM_CARDS = [
    {
        "name": "COM-01: CRM Hub / Hub de Gestión CRM",
        "desc": """## COM-01: Customer Relationship Management Hub

### User Story
**As a** Sales Director,
**I want** a unified CRM hub integrated with operations data
**So that** I can maintain a 360° view of customer relationships.

**Story Points**: 13 | **Priority**: High | **Epic**: Sales & Commercial

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | CRM Integration Module |
| Dependencies | LOG-02 (Inventory), PROD-01 (Sprint), FAC-01 (Invoicing) |
| UI | React with customer timeline visualization |
| API | Laravel with CRM sync adapters |

### Risk Summary
- Data silos → API-first integration with MDM
- Low adoption → Mobile-first UX with minimal data entry
- Stale inventory → Real-time sync with LOG-02

---

## COM-01: Hub de Gestión de Relaciones con Clientes

### Historia de Usuario
**Como** Director de Ventas,
**Quiero** un hub CRM unificado integrado con datos operativos
**Para** poder mantener una visión 360° de las relaciones con clientes.

**Story Points**: 13 | **Prioridad**: Alta | **Epic**: Ventas y Comercial

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Integración CRM |
| Dependencias | LOG-02 (Inventario), PROD-01 (Sprint), FAC-01 (Facturación) |
| UI | React con visualización de línea temporal |
| API | Laravel con adaptadores de sincronización CRM |

### Resumen de Riesgos
- Silos de datos → Integración API-first con MDM
- Baja adopción → UX mobile-first con mínima entrada de datos
- Inventario obsoleto → Sincronización en tiempo real con LOG-02""",
        "checklist": [
            "Customer profiles aggregate all touchpoints / Perfiles agregan todos los touchpoints",
            "Interaction timeline displays last 100 activities / Timeline muestra últimas 100 actividades",
            "Pipeline supports custom stages / Pipeline soporta etapas personalizadas",
            "Inventory visibility when creating quotes / Visibilidad de inventario al crear cotizaciones",
            "Lead scoring updates on 10+ signals / Lead scoring actualiza con 10+ señales",
            "Territory assignments prevent duplicates / Territorios previenen duplicados",
            "Mobile app supports offline with sync / App móvil soporta offline con sync",
            "Search returns results in < 300ms / Búsqueda retorna en < 300ms",
            "GDPR compliance for data handling / Compliance GDPR para datos",
            "Integration with LOG-02 for delivery dates / Integración con LOG-02 para fechas",
            "Dashboard shows KPIs: pipeline, win rate / Dashboard muestra KPIs"
        ]
    },
    {
        "name": "COM-02: Retention Engine / Motor de Retención",
        "desc": """## COM-02: Customer Retention & Loyalty Engine

### User Story
**As a** Customer Success Manager,
**I want** a predictive retention engine that identifies at-risk customers
**So that** I can proactively prevent churn and maximize CLV.

**Story Points**: 13 | **Priority**: High | **Epic**: Sales & Commercial

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Retention Analytics Module |
| Dependencies | COM-01 (CRM), LOG-01 (Lead Time), FAC-02 (Payment) |
| UI | React with churn prediction dashboards |
| API | Laravel with ML model integration |

### Risk Summary
- Prediction bias → Regular model fairness audits
- Alert fatigue → Tiered severity with actionable guidance
- Privacy concerns → Transparent policies with opt-outs

---

## COM-02: Motor de Retención y Lealtad de Clientes

### Historia de Usuario
**Como** Customer Success Manager,
**Quiero** un motor de retención predictivo que identifique clientes en riesgo
**Para** poder prevenir churn proactivamente y maximizar CLV.

**Story Points**: 13 | **Prioridad**: Alta | **Epic**: Ventas y Comercial

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Analítica de Retención |
| Dependencias | COM-01 (CRM), LOG-01 (Lead Time), FAC-02 (Pagos) |
| UI | React con dashboards de predicción de churn |
| API | Laravel con integración de modelos ML |

### Resumen de Riesgos
- Sesgo de predicción → Auditorías de equidad del modelo
- Fatiga de alertas → Severidad escalonada con guía accionable
- Privacidad → Políticas transparentes con opt-outs""",
        "checklist": [
            "Churn prediction 80% accuracy at 30 days / Predicción de churn 80% a 30 días",
            "Health score from 15+ weighted indicators / Health score de 15+ indicadores",
            "At-risk alerts trigger workflows / Alertas de riesgo disparan workflows",
            "Cohort retention charts compare groups / Gráficos de cohorte comparan grupos",
            "Win-back campaigns track success / Campañas de recuperación rastrean éxito",
            "Sentiment scores from support tickets / Scores de sentimiento de tickets",
            "Loyalty tiers apply benefits automatically / Niveles de lealtad aplican beneficios",
            "CLV calculated and displayed / CLV calculado y mostrado",
            "Retention dashboards for executives / Dashboards de retención para ejecutivos",
            "Integration with LOG-01 correlates delays / Integración con LOG-01 correlaciona retrasos",
            "A/B testing for retention interventions / A/B testing para intervenciones"
        ]
    },
    {
        "name": "COM-03: VoC Feedback System / Sistema de Feedback VoC",
        "desc": """## COM-03: Voice of Customer Feedback System

### User Story
**As a** Product Manager,
**I want** a systematic feedback collection and analysis platform
**So that** I can translate customer insights into product improvements.

**Story Points**: 8 | **Priority**: Medium | **Epic**: Sales & Commercial

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | VoC Analytics Module |
| Dependencies | PROD-02 (Backlog), COM-01 (CRM), PROD-05 (Hub) |
| UI | React with sentiment visualization |
| API | Laravel with NLP processing pipeline |

### Risk Summary
- Low survey response rates → Incentivized micro-surveys
- NLP misclassification → Human review loop for training
- Feedback overload → Prioritization scoring

---

## COM-03: Sistema de Feedback Voz del Cliente

### Historia de Usuario
**Como** Product Manager,
**Quiero** una plataforma sistemática de recolección y análisis de feedback
**Para** poder traducir insights de clientes en mejoras de producto.

**Story Points**: 8 | **Prioridad**: Media | **Epic**: Ventas y Comercial

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Analítica VoC |
| Dependencias | PROD-02 (Backlog), COM-01 (CRM), PROD-05 (Hub) |
| UI | React con visualización de sentimiento |
| API | Laravel con pipeline de procesamiento NLP |

### Resumen de Riesgos
- Bajas tasas de respuesta → Micro-encuestas incentivadas
- Mala clasificación NLP → Loop de revisión humana
- Sobrecarga de feedback → Scoring de priorización""",
        "checklist": [
            "Feedback from 5+ channels unified / Feedback de 5+ canales unificado",
            "NLP extracts themes with 75% accuracy / NLP extrae temas con 75% precisión",
            "Sentiment trends over time / Tendencias de sentimiento en tiempo",
            "Feedback linkable to PROD-02 backlog / Feedback vinculable a backlog PROD-02",
            "Survey triggers after key events / Encuestas tras eventos clave",
            "Competitive mentions flagged / Menciones competitivas marcadas",
            "Response templates reduce time 50% / Plantillas reducen tiempo 50%",
            "NPS score calculated monthly / Score NPS calculado mensualmente",
            "Volume and response rates tracked / Volumen y tasas rastreadas",
            "Executive VoC dashboard / Dashboard ejecutivo de VoC",
            "Integration with PROD-05 for reporting / Integración con PROD-05"
        ]
    },
    {
        "name": "COM-04: Revenue Analytics / Analítica de Ingresos",
        "desc": """## COM-04: Revenue Growth & Pipeline Analytics

### User Story
**As a** Chief Revenue Officer,
**I want** comprehensive pipeline analytics with growth forecasting
**So that** I can make data-driven decisions on targets and allocation.

**Story Points**: 13 | **Priority**: High | **Epic**: Sales & Commercial

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Revenue Analytics Module |
| Dependencies | COM-01 (CRM), FAC-03 (Cash Flow), LOG-02 (Inventory) |
| UI | React with advanced charting (D3.js) |
| API | Laravel with forecasting algorithms |

### Risk Summary
- Inaccurate opportunity data → Data quality rules
- Sales/delivery disconnect → Integrated capacity signals
- Historical pattern over-reliance → Ensemble forecasting

---

## COM-04: Analítica de Crecimiento e Ingresos

### Historia de Usuario
**Como** Chief Revenue Officer,
**Quiero** analítica integral de pipeline con pronóstico de crecimiento
**Para** poder tomar decisiones basadas en datos sobre objetivos y asignación.

**Story Points**: 13 | **Prioridad**: Alta | **Epic**: Ventas y Comercial

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Analítica de Ingresos |
| Dependencias | COM-01 (CRM), FAC-03 (Cash Flow), LOG-02 (Inventario) |
| UI | React con charting avanzado (D3.js) |
| API | Laravel con algoritmos de pronóstico |

### Resumen de Riesgos
- Datos imprecisos de oportunidades → Reglas de calidad
- Desconexión ventas/entrega → Señales de capacidad integradas
- Sobre-dependencia de patrones → Pronóstico ensemble""",
        "checklist": [
            "Pipeline funnel shows conversion rates / Funnel muestra tasas de conversión",
            "Forecast accuracy within 10% of actuals / Precisión dentro del 10%",
            "Quota dashboards in real-time / Dashboards de cuota en tiempo real",
            "Segment analysis identifies opportunities / Análisis de segmento identifica oportunidades",
            "Velocity metrics weekly trending / Métricas de velocidad con tendencia semanal",
            "PROD capacity constraints flagged / Restricciones de capacidad PROD señaladas",
            "3+ scenario models supported / 3+ modelos de escenario soportados",
            "MRR tracked / MRR rastreado",
            "Bookings vs billings reconciled / Reservas vs facturación reconciliados",
            "Board-ready reports exportable / Reportes para junta exportables",
            "Integration with FAC-03 for cash flow / Integración con FAC-03"
        ]
    },
    {
        "name": "COM-05: CX Platform / Plataforma de Experiencia",
        "desc": """## COM-05: Customer Experience Platform

### User Story
**As a** Customer Experience Director,
**I want** an integrated platform measuring satisfaction across touchpoints
**So that** I can ensure consistent experiences that drive advocacy.

**Story Points**: 8 | **Priority**: Medium | **Epic**: Sales & Commercial

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | CX Platform Module |
| Dependencies | COM-01, COM-03, LOG-01, PROD-05 |
| UI | React with journey mapping visualization |
| API | Laravel with event-driven CX tracking |

### Risk Summary
- Touchpoint gaps → Comprehensive journey audit
- Survey fatigue → Strategic placement with sampling
- Slow service recovery → Automated escalation with SLA

---

## COM-05: Plataforma de Experiencia del Cliente

### Historia de Usuario
**Como** Director de Customer Experience,
**Quiero** una plataforma integrada que mida satisfacción en todos los touchpoints
**Para** poder asegurar experiencias consistentes que impulsen advocacy.

**Story Points**: 8 | **Prioridad**: Media | **Epic**: Ventas y Comercial

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Plataforma CX |
| Dependencias | COM-01, COM-03, LOG-01, PROD-05 |
| UI | React con visualización de mapeo de journey |
| API | Laravel con tracking CX event-driven |

### Resumen de Riesgos
- Gaps de touchpoints → Auditoría comprehensiva de journey
- Fatiga de encuestas → Colocación estratégica con muestreo
- Recuperación lenta → Escalamiento automatizado con SLA""",
        "checklist": [
            "Journey maps define 10+ touchpoints / Mapas definen 10+ touchpoints",
            "CSAT surveys at 5+ critical points / Encuestas CSAT en 5+ puntos",
            "Experience gaps quantified / Gaps de experiencia cuantificados",
            "Service recovery within 2 hours / Recuperación en 2 horas",
            "Referral tracking attributes customers / Tracking de referidos atribuye clientes",
            "Industry benchmarks displayed / Benchmarks de industria mostrados",
            "Initiatives linked to metrics / Iniciativas vinculadas a métricas",
            "CES measured for key processes / CES medido para procesos clave",
            "Executive CX dashboard / Dashboard ejecutivo de CX",
            "Integration with LOG-01 for delivery / Integración con LOG-01 para entrega",
            "Advocacy program tracks promoters / Programa rastrea promotores"
        ]
    }
]

# Finance cards
FAC_CARDS = [
    {
        "name": "FAC-01: Invoicing & Collections / Facturación y Cobros",
        "desc": """## FAC-01: Integrated Invoicing & Collections System

### User Story
**As a** Finance Director,
**I want** an integrated invoicing and collections system
**So that** I can automate billing cycles and reduce DSO.

**Story Points**: 13 | **Priority**: High | **Epic**: Finance & Billing

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Billing & Collections Module |
| Dependencies | COM-01 (CRM), LOG-02 (Inventory), ERP |
| UI | React with invoice management interface |
| API | Laravel with payment gateway integrations |

### Risk Summary
- Gateway downtime → Multiple failover configuration
- Tax errors → Regular table updates with audit logs
- Invoice disputes → Clear resolution workflow

---

## FAC-01: Sistema Integrado de Facturación y Cobros

### Historia de Usuario
**Como** Director de Finanzas,
**Quiero** un sistema integrado de facturación y cobros
**Para** poder automatizar ciclos de facturación y reducir DSO.

**Story Points**: 13 | **Prioridad**: Alta | **Epic**: Finanzas y Facturación

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Facturación y Cobros |
| Dependencias | COM-01 (CRM), LOG-02 (Inventario), ERP |
| UI | React con interfaz de gestión de facturas |
| API | Laravel con integraciones de pasarela |

### Resumen de Riesgos
- Caída de pasarela → Configuración de failover múltiple
- Errores fiscales → Actualizaciones regulares con auditoría
- Disputas de facturas → Workflow claro de resolución""",
        "checklist": [
            "Invoices generated on LOG delivery / Facturas generadas en entrega LOG",
            "3+ billing models configurable / 3+ modelos de facturación",
            "2+ payment gateway integrations / 2+ integraciones de pasarela",
            "Dunning at 7, 14, 30 days / Dunning a los 7, 14, 30 días",
            "Credit holds when limits exceeded / Retenciones cuando se exceden límites",
            "10+ currencies with daily rates / 10+ monedas con tasas diarias",
            "Accurate tax calculations / Cálculos fiscales precisos",
            "PDF invoices with templates / Facturas PDF con plantillas",
            "Payment reconciliation automated / Conciliación de pagos automatizada",
            "DSO metrics displayed daily / Métricas DSO mostradas diariamente",
            "Integration with COM-01 for status / Integración con COM-01"
        ]
    },
    {
        "name": "FAC-02: Production Cost Audit / Auditoría de Costos",
        "desc": """## FAC-02: Production Cost Audit & Analysis

### User Story
**As a** Controller,
**I want** a comprehensive production cost auditing system
**So that** I can track variances and optimize efficiency.

**Story Points**: 13 | **Priority**: High | **Epic**: Finance & Billing

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Cost Analytics Module |
| Dependencies | PROD-01 (Sprint), LOG-02 (Inventory), PROD-03 (Velocity) |
| UI | React with cost variance dashboards |
| API | Laravel with cost allocation engine |

### Risk Summary
- Incomplete time tracking → Mandatory entry with reminders
- Complex allocation rules → Clear methodology documentation
- Delayed cost data → Real-time feeds from source systems

---

## FAC-02: Auditoría y Análisis de Costos de Producción

### Historia de Usuario
**Como** Controller,
**Quiero** un sistema integral de auditoría de costos de producción
**Para** poder rastrear varianzas y optimizar eficiencia.

**Story Points**: 13 | **Prioridad**: Alta | **Epic**: Finanzas y Facturación

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Analítica de Costos |
| Dependencias | PROD-01 (Sprint), LOG-02 (Inventario), PROD-03 (Velocidad) |
| UI | React con dashboards de varianza de costos |
| API | Laravel con motor de asignación |

### Resumen de Riesgos
- Tracking de tiempo incompleto → Entrada obligatoria con recordatorios
- Reglas complejas → Documentación clara de metodología
- Datos retrasados → Feeds en tiempo real desde sistemas fuente""",
        "checklist": [
            "Cost drivers for 5+ activity types / Drivers para 5+ tipos de actividad",
            "Variance reports budget vs actual / Reportes de varianza presupuesto vs real",
            "Labor costs from PROD-01 sprint data / Costos laborales de datos PROD-01",
            "Material costs from LOG-02 consumption / Costos de materiales de LOG-02",
            "Overhead rates by department / Tasas de overhead por departamento",
            "Cost center hierarchy 4+ levels / Jerarquía de centros de costo 4+ niveles",
            "Project margins real-time / Márgenes de proyecto en tiempo real",
            "Variance alerts at 10% threshold / Alertas de varianza al 10%",
            "Monthly cost reports automated / Reportes mensuales automatizados",
            "YoY cost trend analysis / Análisis de tendencia año sobre año",
            "Integration with PROD-03 for velocity-cost / Integración con PROD-03"
        ]
    },
    {
        "name": "FAC-03: Cash Flow Forecasting / Pronóstico de Cash Flow",
        "desc": """## FAC-03: Cash Flow Forecasting & Treasury

### User Story
**As a** CFO,
**I want** an intelligent cash flow forecasting system
**So that** I can anticipate liquidity needs and optimize working capital.

**Story Points**: 21 | **Priority**: High | **Epic**: Finance & Billing

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Treasury & Cash Flow Module |
| Dependencies | FAC-01 (Invoicing), COM-04 (Revenue), LOG-02 (Inventory) |
| UI | React with cash flow visualization |
| API | Laravel with predictive modeling |

### Risk Summary
- Forecast inaccuracy → Conservative buffers with scenarios
- Bank integration delays → Multiple data source redundancy
- Covenant breach risk → Early warning at 90% threshold

---

## FAC-03: Pronóstico de Cash Flow y Tesorería

### Historia de Usuario
**Como** CFO,
**Quiero** un sistema inteligente de pronóstico de cash flow
**Para** poder anticipar necesidades de liquidez y optimizar capital de trabajo.

**Story Points**: 21 | **Prioridad**: Alta | **Epic**: Finanzas y Facturación

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Tesorería y Cash Flow |
| Dependencias | FAC-01 (Facturación), COM-04 (Ingresos), LOG-02 (Inventario) |
| UI | React con visualización de cash flow |
| API | Laravel con modelado predictivo |

### Resumen de Riesgos
- Imprecisión de pronóstico → Buffers conservadores con escenarios
- Retrasos de integración bancaria → Redundancia de fuentes de datos
- Riesgo de violación de covenants → Advertencia temprana al 90%""",
        "checklist": [
            "13-week rolling forecast / Pronóstico rodante de 13 semanas",
            "3 scenarios with probability weights / 3 escenarios con pesos",
            "Bank balances sync within 4 hours / Saldos bancarios sync en 4 horas",
            "Working capital metrics (DSO, DPO, DIO) / Métricas de capital de trabajo",
            "Surplus cash flagged for investment / Excedente señalado para inversión",
            "Covenant ratios monitored / Ratios de covenants monitoreados",
            "FX exposure quantified / Exposición FX cuantificada",
            "Forecast accuracy tracked / Precisión de pronóstico rastreada",
            "Cash flow statement automated / Estado de cash flow automatizado",
            "Board reports exportable / Reportes para junta exportables",
            "Integration with COM-04 for projections / Integración con COM-04"
        ]
    },
    {
        "name": "FAC-04: Tax Compliance / Cumplimiento Fiscal",
        "desc": """## FAC-04: Tax Compliance & Regulatory Reporting

### User Story
**As a** Tax Manager,
**I want** an automated tax compliance and reporting system
**So that** I can ensure timely filings and minimize compliance risk.

**Story Points**: 13 | **Priority**: Medium | **Epic**: Finance & Billing

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Tax Compliance Module |
| Dependencies | FAC-01 (Invoicing), FAC-02 (Costs), ERP |
| UI | React with compliance calendar |
| API | Laravel with tax authority API integrations |

### Risk Summary
- Missed deadlines → Automated reminders with escalation
- Incorrect calculations → Dual-check with external rates
- Regulation changes → Subscription to regulatory updates

---

## FAC-04: Cumplimiento Fiscal y Reporting Regulatorio

### Historia de Usuario
**Como** Tax Manager,
**Quiero** un sistema automatizado de cumplimiento y reporting fiscal
**Para** poder asegurar presentaciones oportunas y minimizar riesgo de compliance.

**Story Points**: 13 | **Prioridad**: Media | **Epic**: Finanzas y Facturación

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de Cumplimiento Fiscal |
| Dependencias | FAC-01 (Facturación), FAC-02 (Costos), ERP |
| UI | React con calendario de compliance |
| API | Laravel con integraciones de API fiscales |

### Resumen de Riesgos
- Fechas perdidas → Recordatorios automatizados con escalamiento
- Cálculos incorrectos → Doble verificación con tasas externas
- Cambios regulatorios → Suscripción a actualizaciones regulatorias""",
        "checklist": [
            "Tax calendar tracks all jurisdictions / Calendario rastrea jurisdicciones",
            "VAT returns auto-generated / Declaraciones de IVA auto-generadas",
            "Transfer pricing templates available / Plantillas de precios de transferencia",
            "Tax provision calculated quarterly / Provisión calculada trimestralmente",
            "Audit trail for all determinations / Pista de auditoría para determinaciones",
            "E-filing for 3+ jurisdictions / E-filing para 3+ jurisdicciones",
            "Withholding rates correct / Tasas de retención correctas",
            "Filing reminders 30/15/7 days / Recordatorios 30/15/7 días",
            "Tax rate updates within 24 hours / Actualizaciones de tasas en 24 horas",
            "Audit-ready reports on demand / Reportes para auditoría on demand",
            "Integration with FAC-01 for accuracy / Integración con FAC-01"
        ]
    },
    {
        "name": "FAC-05: Financial Analytics BI / Analítica Financiera",
        "desc": """## FAC-05: Financial Analytics & Business Intelligence

### User Story
**As a** VP of Finance,
**I want** a comprehensive financial analytics platform
**So that** I can provide strategic insights and support data-driven decisions.

**Story Points**: 13 | **Priority**: Medium | **Epic**: Finance & Billing

### Technical Context
| Aspect | Details |
|--------|---------|
| Component | Financial BI Module |
| Dependencies | All FAC modules, COM-04, PROD-05 |
| UI | React with executive dashboard suite |
| API | Laravel with data warehouse integration |

### Risk Summary
- Data quality issues → Validation rules with quality scores
- Dashboard overload → Role-based progressive disclosure
- Stale data → Clear timestamps and refresh indicators

---

## FAC-05: Analítica Financiera e Inteligencia de Negocios

### Historia de Usuario
**Como** VP de Finanzas,
**Quiero** una plataforma integral de analítica financiera
**Para** poder proveer insights estratégicos y soportar decisiones basadas en datos.

**Story Points**: 13 | **Prioridad**: Media | **Epic**: Finanzas y Facturación

### Contexto Técnico
| Aspecto | Detalles |
|---------|----------|
| Componente | Módulo de BI Financiero |
| Dependencias | Todos los módulos FAC, COM-04, PROD-05 |
| UI | React con suite de dashboards ejecutivos |
| API | Laravel con integración de data warehouse |

### Resumen de Riesgos
- Problemas de calidad de datos → Reglas con scores de calidad
- Sobrecarga de dashboard → Divulgación progresiva por rol
- Datos obsoletos → Timestamps claros e indicadores de refresh""",
        "checklist": [
            "KPI dashboard with 15+ metrics / Dashboard con 15+ métricas",
            "Period comparisons (MoM, QoQ, YoY) / Comparaciones de período",
            "Profitability drillable to customer / Rentabilidad drillable a cliente",
            "What-if scenarios with 3+ drivers / Escenarios what-if con 3+ drivers",
            "Narrative summaries for variances / Resúmenes narrativos para varianzas",
            "Industry benchmarks displayed / Benchmarks de industria mostrados",
            "Self-service report builder / Constructor de reportes self-service",
            "Data refresh within 1 hour / Refresh de datos en 1 hora",
            "Mobile-optimized executive view / Vista ejecutiva optimizada para móvil",
            "Subscription alerts for thresholds / Alertas de suscripción para umbrales",
            "Integration with PROD-05 for unified view / Integración con PROD-05"
        ]
    }
]

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

def create_card(name, idList, idLabels):
    """Create a new card."""
    url = f"https://api.trello.com/1/cards"
    data = {"key": KEY, "token": TOKEN, "name": name, "idList": idList, "idLabels": idLabels}
    return make_request(url, data, "POST")

def update_card_desc(card_id, desc):
    """Update card description."""
    url = f"https://api.trello.com/1/cards/{card_id}"
    data = {"key": KEY, "token": TOKEN, "desc": desc}
    return make_request(url, data, "PUT")

def create_checklist(card_id, items):
    """Create checklist with items."""
    url = f"https://api.trello.com/1/checklists"
    data = {"key": KEY, "token": TOKEN, "idCard": card_id, "name": "Acceptance Criteria / Criterios de Aceptación"}
    result = make_request(url, data, "POST")
    
    if not result:
        return
    
    checklist_id = result["id"]
    
    for item in items:
        url = f"https://api.trello.com/1/checklists/{checklist_id}/checkItems"
        data = {"key": KEY, "token": TOKEN, "name": item}
        make_request(url, data, "POST")
    
    return checklist_id

def process_cards(cards, label_id, epic_name):
    """Process a list of cards."""
    print(f"\n{'='*60}")
    print(f"Creating {epic_name} Cards")
    print(f"{'='*60}")
    
    for card_config in cards:
        print(f"\n📋 Creating: {card_config['name'][:50]}...")
        
        result = create_card(card_config["name"], BACKLOG_LIST_ID, label_id)
        if not result:
            print(f"   ❌ Failed to create card")
            continue
        
        card_id = result["id"]
        print(f"   ✅ Card created: {card_id}")
        
        update_card_desc(card_id, card_config["desc"])
        print(f"   ✅ Description updated")
        
        create_checklist(card_id, card_config["checklist"])
        print(f"   ✅ Checklist added with {len(card_config['checklist'])} items")

def main():
    """Main execution."""
    if not KEY or not TOKEN:
        print("Error: TRELLO_KEY and TRELLO_TOKEN environment variables must be set")
        return
    
    print("=" * 60)
    print("NexusFlow - Creating Sales & Finance Cards")
    print("=" * 60)
    
    # Create Commercial cards
    process_cards(COM_CARDS, COMERCIAL_LABEL_ID, "Commercial (Green)")
    
    # Create Finance cards
    process_cards(FAC_CARDS, FACTURACION_LABEL_ID, "Finance (Yellow)")
    
    print("\n" + "=" * 60)
    print("✅ All Sales & Finance cards created successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
