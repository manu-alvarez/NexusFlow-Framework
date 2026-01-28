#!/usr/bin/env python3
"""Generate NexusFlow simple guide PDF with screenshots."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from PIL import Image as PILImage
import os

# Paths
DOCS_DIR = "/Users/manu/Desktop/NexusFlow/docs"
OUTPUT_PDF = os.path.join(DOCS_DIR, "NexusFlow_Guia_Sencilla.pdf")
IMG_BOARD = os.path.join(DOCS_DIR, "img_board_overview.png")
IMG_BLOCKER = os.path.join(DOCS_DIR, "img_blocker.png")
IMG_DASHBOARD = os.path.join(DOCS_DIR, "img_dashboard.png")

# Colors
BLUE = HexColor("#1E88E5")
ORANGE = HexColor("#FB8C00")
GREEN = HexColor("#43A047")
YELLOW = HexColor("#FDD835")
DARK = HexColor("#263238")

def create_pdf():
    """Create the PDF guide."""
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=DARK,
        alignment=TA_CENTER,
        spaceAfter=0.3*cm
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=HexColor("#546E7A"),
        alignment=TA_CENTER,
        spaceAfter=0.5*cm
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=BLUE,
        spaceBefore=0.4*cm,
        spaceAfter=0.3*cm
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=DARK,
        spaceAfter=0.2*cm,
        leading=14
    )
    
    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor("#78909C"),
        alignment=TA_CENTER,
        spaceBefore=0.1*cm,
        spaceAfter=0.3*cm
    )
    
    story = []
    
    # === PAGE 1 ===
    
    # Title
    story.append(Paragraph("📊 NexusFlow", title_style))
    story.append(Paragraph("Guía Sencilla de tu Sistema de Gestión", subtitle_style))
    story.append(Spacer(1, 0.3*cm))
    
    # What is NexusFlow?
    story.append(Paragraph("🤔 ¿Qué es NexusFlow?", heading_style))
    story.append(Paragraph(
        "Imagina que tu trabajo es como una cocina ocupada. Tienes pedidos entrando, "
        "ingredientes que organizar, platos que cocinar y entregas que hacer. "
        "<b>NexusFlow es tu receta maestra</b> que conecta todo: desde que llega el pedido "
        "hasta que el cliente paga feliz.",
        body_style
    ))
    story.append(Paragraph(
        "En lugar de tener notas por todos lados, todo está en <b>un solo tablero visual</b> "
        "donde puedes ver qué está pasando en cada momento.",
        body_style
    ))
    story.append(Spacer(1, 0.2*cm))
    
    # The 4 Epics
    story.append(Paragraph("🎨 Las 4 Áreas del Negocio (Épicas)", heading_style))
    story.append(Paragraph(
        "Cada color representa una parte importante de la operación:",
        body_style
    ))
    
    # Epic table
    epic_data = [
        ["🔵 Producción", "Lo que creamos: sprints, velocidad, planificación"],
        ["🟠 Logística", "Lo que movemos: inventario, proveedores, entregas"],
        ["🟢 Comercial", "Lo que vendemos: clientes, CRM, retención"],
        ["🟡 Facturación", "Lo que cobramos: facturas, costos, impuestos"]
    ]
    
    epic_table = Table(epic_data, colWidths=[4*cm, 12*cm])
    epic_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), HexColor("#ECEFF1")),
        ('TEXTCOLOR', (0, 0), (-1, -1), DARK),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#CFD8DC")),
    ]))
    story.append(epic_table)
    story.append(Spacer(1, 0.3*cm))
    
    # Board image
    if os.path.exists(IMG_BOARD):
        img = Image(IMG_BOARD, width=17*cm, height=5.5*cm)
        story.append(img)
        story.append(Paragraph(
            "📸 Vista del tablero Trello: cada columna es una etapa del trabajo",
            caption_style
        ))
    
    # === PAGE 2 ===
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph("📋 ¿Cómo Trabajo en el Día a Día?", heading_style))
    story.append(Paragraph(
        "El trabajo fluye de izquierda a derecha, como una línea de producción:",
        body_style
    ))
    
    # Flow explanation
    flow_text = """
    <b>1. PRODUCT BACKLOG</b> → Las ideas y tareas pendientes esperan aquí<br/>
    <b>2. SPRINT PLANNING</b> → Selecciono las tareas para esta semana<br/>
    <b>3. IN PROGRESS</b> → Trabajo activamente en estas tareas<br/>
    <b>4. BLOCKERS</b> → Si algo me detiene, lo pongo aquí para buscar ayuda<br/>
    <b>5. DONE</b> → ¡Celebramos! La tarea está completada
    """
    story.append(Paragraph(flow_text, body_style))
    story.append(Spacer(1, 0.2*cm))
    
    # Blocker management
    story.append(Paragraph("⚠️ Cuando Algo Sale Mal (Gestión de Bloqueantes)", heading_style))
    story.append(Paragraph(
        "No escondo los problemas, los hago visibles. Cuando una tarea se bloquea "
        "(ej: esperando credenciales de un proveedor), la muevo a BLOCKERS con un "
        "comentario explicando qué necesito y cuándo lo espero resolver.",
        body_style
    ))
    
    if os.path.exists(IMG_BLOCKER):
        img = Image(IMG_BLOCKER, width=17*cm, height=4.8*cm)
        story.append(img)
        story.append(Paragraph(
            "📸 Tarjeta bloqueada: el equipo puede ver el problema y ayudar a resolverlo",
            caption_style
        ))
    
    # Metrics
    story.append(Paragraph("📈 Métricas en Tiempo Real", heading_style))
    story.append(Paragraph(
        "Un dashboard muestra el progreso: velocidad, eficiencia y bloqueos pendientes. "
        "Así cualquiera puede ver cómo vamos sin preguntar.",
        body_style
    ))
    
    if os.path.exists(IMG_DASHBOARD):
        img = Image(IMG_DASHBOARD, width=17*cm, height=4.3*cm)
        story.append(img)
        story.append(Paragraph(
            "📸 Dashboard de métricas: todo el progreso en un solo vistazo",
            caption_style
        ))
    
    # Conclusion
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("🤖 IA + Mejora Continua", heading_style))
    story.append(Paragraph(
        "Este proyecto fue construido con ayuda de <b>inteligencia artificial</b> (Claude/Antigravity), "
        "demostrando que la IA no reemplaza el criterio humano, sino que lo potencia. "
        "Cada sprint incluye una <b>retrospectiva</b> donde analizo qué funcionó y qué mejorar. "
        "Así el sistema evoluciona constantemente. 🚀",
        body_style
    ))
    
    # Footer
    story.append(Spacer(1, 0.5*cm))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor("#90A4AE"),
        alignment=TA_CENTER
    )
    story.append(Paragraph(
        "NexusFlow Framework v1.0 • Por Manu Alvarez • 2026",
        footer_style
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF created: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_pdf()
