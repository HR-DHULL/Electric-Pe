"""
ElectricPe — Complete Digital Growth Audit & Proposal
McKinsey-Style Professional PDF Generator
By Phone Geetha | work.samsolanki@gmail.com | www.sakshamsolanki.com
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, Wedge
from reportlab.graphics import renderPDF
from reportlab.platypus.flowables import Flowable
import math
import os

# ══════════════════════════════════════════════════
# COLOR PALETTE — McKinsey-inspired deep blue theme
# ══════════════════════════════════════════════════

NAVY      = HexColor("#0B1D3A")
DARK_BLUE = HexColor("#102A50")
MID_BLUE  = HexColor("#1B4F8A")
ACCENT    = HexColor("#2E86DE")
LIGHT_BLUE= HexColor("#D6EAF8")
PALE_BLUE = HexColor("#EBF5FB")
GOLD      = HexColor("#D4A843")
RED       = HexColor("#C0392B")
ORANGE    = HexColor("#E67E22")
GREEN     = HexColor("#27AE60")
DARK_GRAY = HexColor("#2C3E50")
MED_GRAY  = HexColor("#5D6D7E")
LIGHT_GRAY= HexColor("#ECF0F1")
WHITE     = HexColor("#FFFFFF")
CHARCOAL  = HexColor("#1A1A2E")

PAGE_W, PAGE_H = A4
MARGIN = 50

# ══════════════════════════════════════════════════
# CUSTOM FLOWABLES
# ══════════════════════════════════════════════════

class ScoreGauge(Flowable):
    """Circular score gauge — McKinsey-style KPI visual"""
    def __init__(self, score, max_score=100, label="", size=90, color=None):
        Flowable.__init__(self)
        self.score = score
        self.max_score = max_score
        self.label = label
        self.size = size
        if color is None:
            if score < 30: self.color = RED
            elif score < 60: self.color = ORANGE
            elif score < 80: self.color = GOLD
            else: self.color = GREEN
        else:
            self.color = color
        self.width = size
        self.height = size + 30

    def draw(self):
        c = self.canv
        cx, cy = self.size/2, self.size/2 + 20
        r = self.size/2 - 5

        # Background circle
        c.setStrokeColor(LIGHT_GRAY)
        c.setLineWidth(8)
        c.circle(cx, cy, r)

        # Score arc
        angle = (self.score / self.max_score) * 360
        c.setStrokeColor(self.color)
        c.setLineWidth(8)
        c.setLineCap(1)
        # Draw arc using wedge trick
        path = c.beginPath()
        for i in range(int(angle) + 1):
            a = math.radians(90 + i)
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            if i == 0:
                path.moveTo(x, y)
            else:
                path.lineTo(x, y)
        c.drawPath(path, fill=0, stroke=1)

        # Score text
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(self.color)
        txt = f"{self.score}"
        c.drawCentredString(cx, cy - 8, txt)

        c.setFont("Helvetica", 8)
        c.setFillColor(MED_GRAY)
        c.drawCentredString(cx, cy - 20, f"/ {self.max_score}")

        # Label
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(DARK_GRAY)
        c.drawCentredString(cx, 5, self.label)


class ColorBar(Flowable):
    """Horizontal progress bar"""
    def __init__(self, value, max_val=100, width=200, height=14, label="", color=None):
        Flowable.__init__(self)
        self.value = value
        self.max_val = max_val
        self.bar_width = width
        self.bar_height = height
        self.label = label
        self.width = width
        self.height = height + 18
        if color is None:
            if value < 30: self.color = RED
            elif value < 60: self.color = ORANGE
            else: self.color = GREEN
        else:
            self.color = color

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(LIGHT_GRAY)
        c.roundRect(0, 0, self.bar_width, self.bar_height, 4, fill=1, stroke=0)
        # Filled portion
        fill_w = (self.value / self.max_val) * self.bar_width
        c.setFillColor(self.color)
        c.roundRect(0, 0, max(fill_w, 8), self.bar_height, 4, fill=1, stroke=0)
        # Label + value
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(DARK_GRAY)
        c.drawString(0, self.bar_height + 4, self.label)
        c.drawRightString(self.bar_width, self.bar_height + 4, f"{self.value}/{self.max_val}")


class SectionDivider(Flowable):
    """Full-width section divider with number and title"""
    def __init__(self, number, title, subtitle=""):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.width = PAGE_W - 2*MARGIN
        self.height = 60

    def draw(self):
        c = self.canv
        w = self.width
        # Background bar
        c.setFillColor(NAVY)
        c.roundRect(0, 0, w, 50, 6, fill=1, stroke=0)
        # Section number circle
        c.setFillColor(GOLD)
        c.circle(30, 25, 16, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(NAVY)
        c.drawCentredString(30, 19, str(self.number))
        # Title
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(WHITE)
        c.drawString(55, 21, self.title)
        # Subtitle
        if self.subtitle:
            c.setFont("Helvetica", 9)
            c.setFillColor(HexColor("#A0B4CB"))
            c.drawString(55, 7, self.subtitle)


class KeyMetricBox(Flowable):
    """Single KPI metric card"""
    def __init__(self, value, label, color=ACCENT, width=120, height=65):
        Flowable.__init__(self)
        self.value = value
        self.label = label
        self.color = color
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        # Card background
        c.setFillColor(WHITE)
        c.setStrokeColor(LIGHT_GRAY)
        c.setLineWidth(1)
        c.roundRect(0, 0, self.width, self.height, 6, fill=1, stroke=1)
        # Top accent line
        c.setFillColor(self.color)
        c.rect(0, self.height - 4, self.width, 4, fill=1, stroke=0)
        # Value
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(self.color)
        c.drawCentredString(self.width/2, 28, str(self.value))
        # Label
        c.setFont("Helvetica", 7)
        c.setFillColor(MED_GRAY)
        c.drawCentredString(self.width/2, 12, self.label)


class QuoteBox(Flowable):
    """Styled quote/callout box"""
    def __init__(self, text, width=None):
        Flowable.__init__(self)
        self.text = text
        self.box_width = width or (PAGE_W - 2*MARGIN)
        self.width = self.box_width
        self.height = 50

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(PALE_BLUE)
        c.roundRect(0, 0, self.box_width, 44, 6, fill=1, stroke=0)
        # Left accent
        c.setFillColor(ACCENT)
        c.rect(0, 0, 4, 44, fill=1, stroke=0)
        # Text
        c.setFont("Helvetica-Oblique", 10)
        c.setFillColor(DARK_BLUE)
        c.drawString(16, 18, self.text[:100])


# ══════════════════════════════════════════════════
# STYLES
# ══════════════════════════════════════════════════

def get_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'DocTitle', fontName='Helvetica-Bold', fontSize=32,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=6, leading=38
    ))
    styles.add(ParagraphStyle(
        'DocSubtitle', fontName='Helvetica', fontSize=14,
        textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=20, leading=18
    ))
    styles.add(ParagraphStyle(
        'SectionTitle', fontName='Helvetica-Bold', fontSize=18,
        textColor=NAVY, spaceBefore=20, spaceAfter=10, leading=22
    ))
    styles.add(ParagraphStyle(
        'SubSection', fontName='Helvetica-Bold', fontSize=13,
        textColor=DARK_BLUE, spaceBefore=14, spaceAfter=6, leading=16
    ))
    styles.add(ParagraphStyle(
        'SubSubSection', fontName='Helvetica-Bold', fontSize=11,
        textColor=MID_BLUE, spaceBefore=10, spaceAfter=4, leading=14
    ))
    styles.add(ParagraphStyle(
        'Body', fontName='Helvetica', fontSize=9.5,
        textColor=DARK_GRAY, alignment=TA_JUSTIFY, spaceAfter=6,
        leading=14, firstLineIndent=0
    ))
    styles.add(ParagraphStyle(
        'BodyBold', fontName='Helvetica-Bold', fontSize=9.5,
        textColor=DARK_GRAY, spaceAfter=6, leading=14
    ))
    # Override existing Bullet style
    styles.byName['Bullet'] = ParagraphStyle(
        'Bullet', fontName='Helvetica', fontSize=9.5,
        textColor=DARK_GRAY, leftIndent=20, bulletIndent=8,
        spaceAfter=3, leading=13, bulletFontName='Helvetica',
        bulletFontSize=9.5
    )
    styles.add(ParagraphStyle(
        'SmallGray', fontName='Helvetica', fontSize=7.5,
        textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        'Footer', fontName='Helvetica', fontSize=7,
        textColor=MED_GRAY, alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        'CellText', fontName='Helvetica', fontSize=8.5,
        textColor=DARK_GRAY, leading=11
    ))
    styles.add(ParagraphStyle(
        'CellBold', fontName='Helvetica-Bold', fontSize=8.5,
        textColor=DARK_GRAY, leading=11
    ))
    styles.add(ParagraphStyle(
        'CellHeader', fontName='Helvetica-Bold', fontSize=8.5,
        textColor=WHITE, leading=11
    ))
    styles.add(ParagraphStyle(
        'Critical', fontName='Helvetica-Bold', fontSize=8.5,
        textColor=RED, leading=11
    ))
    styles.add(ParagraphStyle(
        'Highlight', fontName='Helvetica-Bold', fontSize=10,
        textColor=ACCENT, spaceAfter=4, leading=13
    ))
    styles.add(ParagraphStyle(
        'BigNumber', fontName='Helvetica-Bold', fontSize=36,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=2
    ))
    return styles


# ══════════════════════════════════════════════════
# TABLE HELPER
# ══════════════════════════════════════════════════

def make_table(headers, rows, col_widths=None, highlight_col=None):
    """Create a styled McKinsey table"""
    s = get_styles()
    data = [[Paragraph(h, s['CellHeader']) for h in headers]]
    for row in rows:
        styled_row = []
        for i, cell in enumerate(row):
            if i == highlight_col:
                styled_row.append(Paragraph(str(cell), s['CellBold']))
            else:
                styled_row.append(Paragraph(str(cell), s['CellText']))
        data.append(styled_row)

    w = col_widths or [int((PAGE_W - 2*MARGIN) / len(headers))] * len(headers)
    t = Table(data, colWidths=w, repeatRows=1)

    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, PALE_BLUE]),
    ]
    t.setStyle(TableStyle(style_cmds))
    return t


def make_status_table(headers, rows, col_widths=None, status_col=None):
    """Table with color-coded status column"""
    s = get_styles()
    data = [[Paragraph(h, s['CellHeader']) for h in headers]]

    for row in rows:
        styled_row = []
        for i, cell in enumerate(row):
            cell_str = str(cell)
            if status_col is not None and i == status_col:
                if 'CRITICAL' in cell_str.upper() or 'FAIL' in cell_str.upper():
                    styled_row.append(Paragraph(cell_str, s['Critical']))
                elif 'PASS' in cell_str.upper() or 'GOOD' in cell_str.upper():
                    st = ParagraphStyle('g', fontName='Helvetica-Bold', fontSize=8.5, textColor=GREEN, leading=11)
                    styled_row.append(Paragraph(cell_str, st))
                else:
                    styled_row.append(Paragraph(cell_str, s['CellBold']))
            else:
                styled_row.append(Paragraph(cell_str, s['CellText']))
        data.append(styled_row)

    w = col_widths or [int((PAGE_W - 2*MARGIN) / len(headers))] * len(headers)
    t = Table(data, colWidths=w, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, PALE_BLUE]),
    ]
    t.setStyle(TableStyle(style_cmds))
    return t


# ══════════════════════════════════════════════════
# PAGE TEMPLATES (Header/Footer)
# ══════════════════════════════════════════════════

def add_page_number(canvas_obj, doc):
    """Add header/footer to every page"""
    canvas_obj.saveState()
    w, h = A4

    # Top bar
    canvas_obj.setFillColor(NAVY)
    canvas_obj.rect(0, h - 28, w, 28, fill=1, stroke=0)
    canvas_obj.setFont("Helvetica-Bold", 7)
    canvas_obj.setFillColor(WHITE)
    canvas_obj.drawString(MARGIN, h - 20, "ELECTRICPE  |  DIGITAL GROWTH AUDIT & PROPOSAL")
    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.drawRightString(w - MARGIN, h - 20, "CONFIDENTIAL  |  MARCH 2026")

    # Gold accent line under header
    canvas_obj.setStrokeColor(GOLD)
    canvas_obj.setLineWidth(2)
    canvas_obj.line(0, h - 29, w, h - 29)

    # Footer
    canvas_obj.setStrokeColor(LIGHT_GRAY)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(MARGIN, 35, w - MARGIN, 35)

    canvas_obj.setFont("Helvetica", 7)
    canvas_obj.setFillColor(MED_GRAY)
    canvas_obj.drawString(MARGIN, 22, "Phone Geetha  |  work.samsolanki@gmail.com  |  www.sakshamsolanki.com")
    canvas_obj.drawRightString(w - MARGIN, 22, f"Page {doc.page}")

    canvas_obj.restoreState()


def add_cover_page(canvas_obj, doc):
    """Custom cover page — no header/footer"""
    pass


# ══════════════════════════════════════════════════
# BUILD THE PDF
# ══════════════════════════════════════════════════

def build_pdf():
    output_path = os.path.join(os.path.dirname(__file__),
                               "ElectricPe_Digital_Audit_PhoneGeetha.pdf")

    doc = BaseDocTemplate(
        output_path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN + 20, bottomMargin=MARGIN
    )

    # Page templates
    frame_normal = Frame(MARGIN, MARGIN, PAGE_W - 2*MARGIN, PAGE_H - 2*MARGIN - 20,
                         id='normal', showBoundary=0)
    frame_cover = Frame(0, 0, PAGE_W, PAGE_H, id='cover', showBoundary=0)

    doc.addPageTemplates([
        PageTemplate(id='Cover', frames=frame_cover, onPage=add_cover_page),
        PageTemplate(id='Normal', frames=frame_normal, onPage=add_page_number),
    ])

    s = get_styles()
    story = []
    usable_w = PAGE_W - 2*MARGIN

    # ═══════════════════════════════════════
    # COVER PAGE
    # ═══════════════════════════════════════

    story.append(Spacer(1, 120))

    # Navy block at top (simulated with table)
    cover_top = Table(
        [[Paragraph("PHONE GEETHA", ParagraphStyle('ct', fontName='Helvetica-Bold',
                     fontSize=12, textColor=GOLD, alignment=TA_CENTER, leading=16))]],
        colWidths=[PAGE_W], rowHeights=[30]
    )
    cover_top.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(cover_top)
    story.append(Spacer(1, 40))

    story.append(Paragraph("ElectricPe", ParagraphStyle(
        'mega', fontName='Helvetica-Bold', fontSize=44, textColor=NAVY,
        alignment=TA_CENTER, leading=50
    )))
    story.append(Paragraph("Digital Growth Audit & Proposal", ParagraphStyle(
        'sub', fontName='Helvetica', fontSize=20, textColor=MID_BLUE,
        alignment=TA_CENTER, leading=26, spaceAfter=8
    )))

    # Gold divider
    story.append(HRFlowable(width="40%", thickness=3, color=GOLD,
                             spaceAfter=20, spaceBefore=10, hAlign='CENTER'))

    story.append(Paragraph("SEO  |  Paid Advertising  |  GTM & Tracking  |  Growth Strategy",
                          ParagraphStyle('tags', fontName='Helvetica', fontSize=11,
                                        textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=30)))

    # Key stats row
    metrics_data = [
        [KeyMetricBox("38/100", "SEO SCORE", RED),
         KeyMetricBox("8/100", "ADS SCORE", RED),
         KeyMetricBox("12/100", "GTM SCORE", RED),
         KeyMetricBox("$3.8B", "MARKET SIZE", GREEN)]
    ]
    metrics_table = Table(metrics_data, colWidths=[usable_w/4]*4, rowHeights=[80])
    metrics_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 30))

    # Cover info box
    info_box_data = [
        [Paragraph("<b>Prepared For:</b>", s['CellText']),
         Paragraph("ElectricPe — India's Largest EV Retail Network", s['CellText'])],
        [Paragraph("<b>Prepared By:</b>", s['CellText']),
         Paragraph("Harsh Dhull, Phone Geetha", s['CellText'])],
        [Paragraph("<b>Contact:</b>", s['CellText']),
         Paragraph("work.samsolanki@gmail.com | www.sakshamsolanki.com", s['CellText'])],
        [Paragraph("<b>Date:</b>", s['CellText']),
         Paragraph("March 17, 2026", s['CellText'])],
        [Paragraph("<b>Classification:</b>", s['CellText']),
         Paragraph("Confidential", s['CellBold'])],
    ]
    info_table = Table(info_box_data, colWidths=[120, usable_w - 120])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PALE_BLUE),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT_BLUE),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(info_table)

    story.append(Spacer(1, 40))
    story.append(Paragraph(
        '"ElectricPe has the scale to dominate India\'s EV search landscape.<br/>'
        'It simply needs to make that scale visible to the digital world."',
        ParagraphStyle('quote', fontName='Helvetica-Oblique', fontSize=11,
                      textColor=MID_BLUE, alignment=TA_CENTER, leading=16)
    ))

    # Switch to Normal template
    from reportlab.platypus.doctemplate import NextPageTemplate
    story.append(NextPageTemplate('Normal'))
    story.append(PageBreak())

    # ═══════════════════════════════════════
    # TABLE OF CONTENTS
    # ═══════════════════════════════════════

    story.append(Paragraph("Table of Contents", s['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=2, color=NAVY, spaceAfter=16))

    toc_items = [
        ("01", "Executive Summary", "The big picture — scores, key findings, revenue impact"),
        ("02", "SEO Audit", "Technical SEO, on-page optimization, content quality, keyword strategy"),
        ("03", "Paid Advertising Audit", "Google Ads, Meta, LinkedIn, YouTube, TikTok — platform-by-platform"),
        ("04", "GTM & Tracking Audit", "Tag management, data layer, conversion tracking, privacy"),
        ("05", "Competitive Landscape", "How ElectricPe stacks up against Statiq, Tata Power, Ather"),
        ("06", "3-Phase Growth Plan", "Week-by-week roadmap: Tracking → SEO + Ads → Scale"),
        ("07", "Budget & ROI Projections", "Investment options, revenue forecasts, payback analysis"),
        ("08", "Service Proposal", "Three engagement options — Foundation, Full-Stack, Performance"),
    ]
    for num, title, desc in toc_items:
        toc_row = Table(
            [[Paragraph(f'<font color="{GOLD.hexval()}">{num}</font>', s['CellBold']),
              Paragraph(f'<b>{title}</b><br/><font size="8" color="{MED_GRAY.hexval()}">{desc}</font>', s['CellText'])]],
            colWidths=[40, usable_w - 40], rowHeights=[36]
        )
        toc_row.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (0,0), 0),
            ('LINEBELOW', (0,0), (-1,-1), 0.5, LIGHT_GRAY),
        ]))
        story.append(toc_row)

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 1: EXECUTIVE SUMMARY
    # ═══════════════════════════════════════

    story.append(SectionDivider(1, "EXECUTIVE SUMMARY", "The state of ElectricPe's digital infrastructure"))
    story.append(Spacer(1, 16))

    story.append(Paragraph("The Opportunity", s['SubSection']))
    story.append(Paragraph(
        "ElectricPe operates in one of India's fastest-growing markets — electric mobility (25-27.6% CAGR, "
        "projected $3.8B by 2033). The company has built genuine product-market fit: 15,000+ charging stations, "
        "35+ Mobility Centres, 6,000+ EVs sold, a 4.4-rated app with 80,000+ community members, and a "
        "Google Maps partnership. Revenue stands at INR 13.3 Cr with $11.4M raised across 8 funding rounds.",
        s['Body']
    ))

    story.append(Paragraph("The Problem", s['SubSection']))
    story.append(Paragraph(
        "Despite this strong foundation, ElectricPe's digital infrastructure is operating at <b>less than 15% "
        "of its potential</b>. The website's SEO foundation has severe structural deficiencies, there is zero "
        "paid advertising on any platform, and the tracking infrastructure is critically broken. Competitors "
        "like Statiq ($18M raised, Y Combinator/Shell-backed), Tata Power EZ Charge, and Ather Energy are "
        "actively investing in digital acquisition while ElectricPe remains invisible online.",
        s['Body']
    ))

    story.append(Spacer(1, 10))

    # Score cards
    story.append(Paragraph("Audit Scores at a Glance", s['SubSection']))

    scores_data = [
        [ScoreGauge(38, 100, "SEO", 80),
         ScoreGauge(8, 100, "ADS", 80),
         ScoreGauge(12, 100, "GTM", 80),
         ScoreGauge(19, 100, "OVERALL", 80, color=RED)]
    ]
    scores_table = Table(scores_data, colWidths=[usable_w/4]*4, rowHeights=[120])
    scores_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(scores_table)
    story.append(Spacer(1, 10))

    # Category breakdown
    story.append(Paragraph("Category Breakdown", s['SubSubSection']))
    story.append(make_status_table(
        ["Category", "Score", "Status", "Key Issue"],
        [
            ["Crawlability & Indexation", "25/100", "CRITICAL", "No XML sitemap; ~15 pages indexed vs 500-2,000 expected"],
            ["URL Structure", "30/100", "CRITICAL", "3 duplicate charging station URLs cannibalizing each other"],
            ["On-Page SEO", "40/100", "POOR", "Missing meta descriptions, H1 tags, weak titles"],
            ["Paid Advertising", "0/100", "CRITICAL", "Zero campaigns on any platform"],
            ["Conversion Tracking", "0/100", "CRITICAL", "No GTM, no GA4, no conversion events"],
            ["Meta Pixel & CAPI", "4/100", "CRITICAL", "Pixel partially deployed; no server-side tracking"],
            ["Content & E-E-A-T", "45/100", "POOR", "Blog underutilized; thin content on key pages"],
            ["Structured Data", "45/100", "POOR", "Missing Organization, BlogPosting, Product schema"],
            ["Security & HTTPS", "80/100", "GOOD", "SSL active; headers need verification"],
        ],
        col_widths=[110, 55, 60, usable_w - 225],
        status_col=2
    ))

    story.append(Spacer(1, 14))

    # Key findings
    story.append(Paragraph("Top 5 Critical Findings", s['SubSection']))
    findings = [
        "<b>1. Zero Paid Advertising Infrastructure</b> — No Google Ads, Meta Ads, LinkedIn Ads, or any tracking pixels installed. ElectricPe has no scalable digital acquisition channel while competitors spend aggressively.",
        "<b>2. Missing XML Sitemap</b> — Google cannot discover 95%+ of ElectricPe's pages. Only ~15 pages are indexed out of an expected 500-2,000+. This single issue suppresses the majority of organic traffic potential.",
        "<b>3. No Conversion Tracking</b> — The INR 299 test ride booking (primary revenue driver) is completely unmeasured. No GTM, no GA4, no data layer. Smart Bidding cannot function. Revenue attribution is impossible.",
        "<b>4. 3-Way URL Cannibalization</b> — Three near-duplicate URLs (/evchargingstations/, /ev-charging-station/, /ev-charging-stations/) compete for the same keyword, diluting ranking signals across all three.",
        "<b>5. Thin JS-Dependent Content</b> — Key landing pages render primarily through client-side JavaScript. Crawlers see little to no indexable content on the most commercially valuable pages.",
    ]
    for f in findings:
        story.append(Paragraph(f, s['Bullet'], bulletText='\u25cf'))
    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 2: SEO AUDIT
    # ═══════════════════════════════════════

    story.append(SectionDivider(2, "SEO AUDIT", "Technical SEO, On-Page, Content Quality & Keyword Strategy"))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Overall SEO Health Score: 38/100", s['SubSection']))
    story.append(Paragraph(
        "ElectricPe's website has severe structural SEO deficiencies that are actively suppressing organic visibility. "
        "The business fundamentals are strong, but the website fails to translate that authority into search engine performance. "
        "Competitors like Statiq and Tata Power EZ Charge are capturing search demand that ElectricPe should own.",
        s['Body']
    ))

    # Crawlability
    story.append(Paragraph("Crawlability & Indexation — CRITICAL", s['SubSection']))
    story.append(make_status_table(
        ["Issue", "Severity", "Detail"],
        [
            ["No XML Sitemap", "CRITICAL", "robots.txt has no Sitemap directive. /sitemap.xml returns empty. Google relies solely on link discovery."],
            ["WordPress paths in Next.js site", "HIGH", "Disallow rule references /wp-content/ — indicates incomplete CMS migration and crawl waste."],
            ["~15 pages indexed (expected 500-2,000+)", "CRITICAL", "Massive gap confirms sitemap + thin content issues are preventing indexation."],
            ["No AI crawler directives", "MEDIUM", "No rules for GPTBot, ClaudeBot, or Google-Extended as AI search grows."],
        ],
        col_widths=[130, 65, usable_w - 195],
        status_col=1
    ))

    story.append(Spacer(1, 10))

    # URL Structure
    story.append(Paragraph("URL Structure — CRITICAL", s['SubSection']))
    story.append(Paragraph(
        "Three URLs compete for the same \"EV charging stations\" queries — the most commercially valuable keyword cluster:",
        s['Body']
    ))
    story.append(make_table(
        ["URL", "Title", "Status"],
        [
            ["/evchargingstations/", "Electric Stations - ElectricPe", "Indexed"],
            ["/ev-charging-station/", "Electricpe Stations Archive", "Indexed"],
            ["/ev-charging-stations/", "EV Charging Stations", "Indexed"],
        ],
        col_widths=[160, 180, usable_w - 340]
    ))
    story.append(Paragraph(
        "<b>Resolution:</b> Consolidate to /ev-charging-stations/ with 301 redirects from the other two. "
        "Update all internal links. This is a 30-minute fix with immediate ranking impact.",
        s['Body']
    ))

    story.append(Spacer(1, 10))

    # On-Page SEO
    story.append(Paragraph("On-Page SEO Issues", s['SubSection']))
    story.append(make_status_table(
        ["Page", "Title Tag", "Meta Description", "H1 Tag", "Verdict"],
        [
            ["Homepage", "Good (63 chars)", "FAIL — Truncated at 125 chars", "VERIFY", "Needs fix"],
            ["About", "PASS (54 chars)", "PASS", "PASS", "Good"],
            ["Charging Stations", "FAIL — Missing 'EV' keyword", "FAIL — Missing entirely", "FAIL — No H1", "Critical"],
            ["Blog", "FAIL — Generic 'Blogs'", "FAIL — Missing entirely", "FAIL — Not visible", "Critical"],
            ["Press", "POOR — Awkward phrasing", "NOT VERIFIED", "VERIFY", "Needs fix"],
        ],
        col_widths=[80, 100, 110, 70, usable_w - 360],
        status_col=4
    ))

    story.append(Spacer(1, 10))

    # Keyword Strategy
    story.append(Paragraph("Keyword Strategy Recommendations", s['SubSection']))
    story.append(make_table(
        ["Tier", "Keywords", "Page Target"],
        [
            ["Tier 1 — Primary", "\"EV charging stations India\", \"buy electric vehicle India\", \"EV charging app\"", "Homepage + Core Pages"],
            ["Tier 2 — Product", "\"EV charging station management software\", \"EV financing India\", \"[city] EV charging\"", "Dedicated Landing Pages"],
            ["Tier 3 — Content", "\"best electric scooter 2026\", \"EV charging cost calculator\", \"FAME subsidy guide\"", "Blog Posts"],
        ],
        col_widths=[90, usable_w - 230, 140]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 3: PAID ADVERTISING AUDIT
    # ═══════════════════════════════════════

    story.append(SectionDivider(3, "PAID ADVERTISING AUDIT", "Google Ads, Meta, LinkedIn, YouTube, TikTok"))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Overall Marketing Health Score: 8/100 — Grade F (Critical)", s['SubSection']))
    story.append(Paragraph(
        "Based on all observable evidence, ElectricPe has essentially zero paid advertising infrastructure in place. "
        "No Meta Pixel, no Google Ads conversion tracking, no LinkedIn Campaign Manager activity, and no evidence "
        "of active paid campaigns on any platform. The score of 8 reflects only positive signals from organic "
        "digital presence (app ratings, WebEngage, WhatsApp widget) that provide a foundation to build on.",
        s['Body']
    ))

    # Platform scores
    story.append(Paragraph("Platform-by-Platform Assessment", s['SubSection']))
    story.append(make_status_table(
        ["Platform", "Score", "Grade", "Status", "Priority"],
        [
            ["Google Ads", "0/100", "FAIL", "Not running — zero campaigns", "Priority 1"],
            ["Meta Ads (FB/IG)", "0/100", "FAIL", "Not running — pixel partial", "Priority 2"],
            ["YouTube Ads", "0/100", "FAIL", "Not running — channel exists", "Priority 3"],
            ["LinkedIn Ads", "0/100", "FAIL", "Not running — no Insight Tag", "Priority 4 (B2B)"],
            ["TikTok Ads", "0/100", "FAIL", "Not running — Phase 3", "Priority 5"],
            ["Microsoft Ads", "N/A", "N/A", "Bing <3% share in India", "Not recommended"],
        ],
        col_widths=[90, 50, 40, 170, usable_w - 350],
        status_col=2
    ))

    story.append(Spacer(1, 10))

    # Google Ads recommended structure
    story.append(Paragraph("Recommended Google Ads Campaign Structure", s['SubSection']))
    story.append(make_table(
        ["Campaign", "Type", "Daily Budget", "Target CPA", "Priority"],
        [
            ["Brand Protection", "Search", "INR 500-1,000", "N/A", "Day 1"],
            ["EV Purchase Intent", "Search", "INR 3,000-5,000", "INR 800-1,500", "Week 2"],
            ["Charging Network", "Search", "INR 1,500-2,500", "INR 500-1,000", "Week 2"],
            ["Retargeting", "Display/Demand Gen", "INR 1,000-2,000", "INR 300-800", "Week 3"],
            ["Performance Max", "PMax", "INR 2,000-4,000", "Data-driven", "Month 3+"],
        ],
        col_widths=[105, 80, 85, 85, usable_w - 355]
    ))

    story.append(Spacer(1, 10))

    # Meta Ads
    story.append(Paragraph("Recommended Meta Ads Campaign Structure", s['SubSection']))
    story.append(make_table(
        ["Campaign", "Objective", "Daily Budget", "Audience", "Creative"],
        [
            ["Test Ride Lead Gen", "Leads", "INR 500-1,000", "Age 22-42, Tier 1-2 cities, EV interests", "Video: test ride experience"],
            ["App Install", "App Installs", "INR 300-500", "Broad urban + retargeting", "Charging station locator demo"],
            ["Retargeting", "Conversions", "INR 200-500", "30-day website visitors", "Testimonials + financing"],
            ["Advantage+ (later)", "Sales", "INR 1,000+", "Automated prospecting", "Combined creative testing"],
        ],
        col_widths=[95, 60, 80, 130, usable_w - 365]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 4: GTM & TRACKING AUDIT
    # ═══════════════════════════════════════

    story.append(SectionDivider(4, "GTM & TRACKING AUDIT", "Tag Management, Data Layer, Conversion Tracking, Privacy"))
    story.append(Spacer(1, 16))

    story.append(Paragraph("GTM Health Score: 12/100 — CRITICAL", s['SubSection']))
    story.append(Paragraph(
        "ElectricPe's tracking infrastructure has fundamental gaps. 0 of 22 GTM checks passed. "
        "The website currently runs WebEngage (ID: in~~2024c260) as its primary CDP, Razorpay for payments, "
        "and a partially deployed Facebook Pixel — none of which substitute for a proper GTM + GA4 stack.",
        s['Body']
    ))

    # What's found vs missing
    story.append(Paragraph("Current Tracking Inventory", s['SubSection']))
    story.append(make_status_table(
        ["Technology", "Status", "Assessment"],
        [
            ["WebEngage SDK v6.0", "FOUND", "Active (in~~2024c260). Not a GTM substitute. Creates vendor lock-in."],
            ["Razorpay Checkout", "FOUND", "Active. Payment events NOT forwarded to any analytics platform."],
            ["Facebook Pixel (fbq)", "PARTIAL", "Reference found in code. Pixel ID unconfirmed. Events unverified."],
            ["WhatsApp Widget", "FOUND", "Active (+91 96328 88926). Click events NOT tracked."],
            ["Google Tag Manager", "NOT FOUND", "CRITICAL — No centralized tag management"],
            ["Google Analytics 4", "NOT FOUND", "CRITICAL — No cross-channel web analytics"],
            ["Google Ads Tag", "NOT FOUND", "CRITICAL — Cannot run Google Ads with conversion optimization"],
            ["Meta CAPI", "NOT FOUND", "CRITICAL — 30-40% conversion data loss from browser restrictions"],
            ["LinkedIn Insight Tag", "NOT FOUND", "CRITICAL — Cannot run LinkedIn Ads or B2B retargeting"],
            ["Consent Management", "NOT FOUND", "MEDIUM — DPDPA 2023 compliance risk"],
        ],
        col_widths=[120, 65, usable_w - 185],
        status_col=1
    ))

    story.append(Spacer(1, 10))

    # Test ride funnel gap
    story.append(Paragraph("The Test Ride Measurement Gap", s['SubSection']))
    story.append(Paragraph(
        "The INR 299 test ride is ElectricPe's most powerful conversion mechanism — a customer who takes "
        "a test ride is estimated to be <b>10x more likely</b> to purchase an EV. Yet this critical event "
        "has ZERO connection to any advertising measurement. No data flows back to Google Ads or Meta. "
        "Smart Bidding has no signal to optimize. You cannot calculate cost-per-test-ride from any channel.",
        s['Body']
    ))

    story.append(Spacer(1, 8))

    # Revenue impact
    story.append(Paragraph("Revenue Impact of Broken Tracking", s['SubSection']))
    story.append(make_table(
        ["Capability", "Current", "After Fix", "Revenue Impact"],
        [
            ["Google Ads Smart Bidding", "Cannot run", "Fully optimized", "INR 3-10L/mo in new test rides"],
            ["Meta Conversion Optimization", "Blind", "Optimized for bookings", "INR 2-5L/mo in new test rides"],
            ["Retargeting", "Zero", "30-day visitor remarketing", "15-25% conversion lift"],
            ["Lookalike Audiences", "Cannot build", "1% from 80K members", "2-3x better CPA"],
            ["Enhanced Conversions", "Not available", "Hashed user data", "+10-15% measured conversions"],
            ["A/B Testing", "Not possible", "GTM-enabled", "5-15% CVR improvement"],
        ],
        col_widths=[120, 80, 110, usable_w - 310]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 5: COMPETITIVE LANDSCAPE
    # ═══════════════════════════════════════

    story.append(SectionDivider(5, "COMPETITIVE LANDSCAPE", "ElectricPe vs. Statiq, Tata Power, Ather, ChargeZone"))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Competitor Digital Advertising Presence", s['SubSection']))
    story.append(make_table(
        ["Competitor", "Funding", "Digital Ad Spend", "Key Advantage"],
        [
            ["Tata Power EZ Charge", "Tata Group", "Very High", "Tata brand equity; 5,500+ stations; unlimited budget"],
            ["Ather Energy", "Hero MotoCorp backed", "Very High", "Premium brand; 800K+ Instagram; strong YouTube"],
            ["Ola Electric", "SoftBank backed", "Very High", "Massive brand spend; TV + digital"],
            ["Statiq", "$18M (YC + Shell)", "High", "65+ cities; 8,000+ chargers; aggressive growth"],
            ["ChargeZone", "Well-funded", "Medium", "B2B charging focus; content marketing"],
            ["Jio-bp Pulse", "Reliance + bp", "Medium-High", "Jio distribution; brand halo"],
            ["ElectricPe", "$11.4M", "ZERO", "15,000+ stations but digitally invisible"],
        ],
        col_widths=[105, 95, 80, usable_w - 280]
    ))

    story.append(Spacer(1, 12))

    story.append(Paragraph("Competitive Gaps ElectricPe Can Exploit", s['SubSection']))
    gaps = [
        "<b>Multi-Brand Dealer Advantage:</b> Ather, Ola, TVS each only advertise their own brand. ElectricPe can target ALL competitor brand keywords: \"Compare 25+ EV models at one place.\"",
        "<b>Physical + Digital Integration:</b> No competitor combines EV retail + charging network + financing. Ad copy: \"Buy, charge, and finance your EV — all in one place.\"",
        "<b>Community as Social Proof:</b> 80,000+ Club Electric members = user-generated content that outperforms corporate ads on Meta and TikTok. Free creative source.",
        "<b>Google Maps Partnership:</b> \"Find ElectricPe stations in real-time on Google Maps\" — a trust signal and convenience argument competitors cannot match.",
        "<b>Regional Language Opportunity:</b> Most competitors run English-only campaigns. Hindi, Kannada, Tamil, Telugu search terms have lower CPCs and less competition.",
    ]
    for g in gaps:
        story.append(Paragraph(g, s['Bullet'], bulletText='\u25cf'))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 6: 3-PHASE GROWTH PLAN
    # ═══════════════════════════════════════

    story.append(SectionDivider(6, "3-PHASE GROWTH PLAN", "Week-by-week: Tracking Foundation → SEO + Ads → Scale"))
    story.append(Spacer(1, 16))

    # Phase 1
    story.append(Paragraph("Phase 1: Tracking Foundation (Weeks 1-3)", s['SubSection']))
    story.append(Paragraph(
        '"You can\'t optimize what you can\'t measure." Before spending a single rupee on ads, '
        "the tracking infrastructure must be bulletproof.",
        s['Body']
    ))
    story.append(make_table(
        ["Week", "Deliverable", "Owner", "Time"],
        [
            ["1", "GTM container on all Next.js pages + dataLayer initialization", "Developer", "6 hrs"],
            ["1", "GA4 configuration with ElectricPe-specific conversion events", "Dev + Analyst", "8 hrs"],
            ["1", "WebEngage migration from inline to GTM (async loading)", "GTM Specialist", "2 hrs"],
            ["2", "Google Ads account + brand campaign + conversion tracking", "Marketing", "6 hrs"],
            ["2", "Meta Pixel verification + standard events + CAPI deployment", "Developer", "8 hrs"],
            ["2", "Enhanced Conversions with hashed user data", "Developer", "3 hrs"],
            ["3", "LinkedIn Insight Tag + consent management platform", "GTM Specialist", "4 hrs"],
            ["3", "Razorpay payment → conversion event integration", "Developer", "4 hrs"],
            ["3", "Cross-domain tracking + Microsoft Clarity (free heatmaps)", "GTM Specialist", "3 hrs"],
        ],
        col_widths=[40, 250, 80, usable_w - 370]
    ))

    story.append(Spacer(1, 12))

    # Phase 2
    story.append(Paragraph("Phase 2: SEO + Paid Ads Launch (Weeks 3-8)", s['SubSection']))
    story.append(make_table(
        ["Action", "Type", "Expected Impact", "Timeline"],
        [
            ["Generate + submit XML sitemaps", "SEO", "10-50x more pages indexed", "Week 3"],
            ["Fix 3-way URL cannibalization", "SEO", "Consolidate ranking power", "Week 3"],
            ["Rewrite all meta titles + descriptions", "SEO", "5-15% CTR improvement", "Week 3-4"],
            ["Launch Google Search campaigns", "Ads", "First paid intent traffic", "Week 4"],
            ["Launch Meta Lead Gen (test ride)", "Ads", "First Meta leads at INR 50-200", "Week 4"],
            ["Launch YouTube TrueView campaigns", "Ads", "EV research journey interception", "Week 5"],
            ["Implement structured data schema", "SEO", "Rich results in Google", "Week 5-6"],
            ["City-specific landing pages (top 5)", "SEO/Ads", "Quality Score + local CVR", "Week 6-8"],
        ],
        col_widths=[160, 40, 155, usable_w - 355]
    ))

    story.append(Spacer(1, 12))

    # Phase 3
    story.append(Paragraph("Phase 3: Scale & Optimize (Months 3-6)", s['SubSection']))
    story.append(make_table(
        ["Month", "Action", "Trigger", "Expected Outcome"],
        [
            ["3", "Enable Smart Bidding (Target CPA)", "30+ conversions/month", "20-30% CPA reduction"],
            ["3", "Launch Meta Advantage+ campaigns", "Lookalike audiences built", "2-3x better CPA vs cold"],
            ["3", "Launch Performance Max (Google)", "Proven conversion data", "Automated reach expansion"],
            ["4", "Launch LinkedIn B2B (fleet + CMS)", "Insight Tag data collected", "Fleet sales pipeline"],
            ["4", "Test TikTok Spark Ads (10% budget)", "Organic content performing", "Young EV buyer awareness"],
            ["5-6", "Scale to 50+ city campaigns", "New Mobility Centres open", "Foot traffic from Day 1"],
            ["5-6", "Regional language ad copy", "Hindi/Kannada/Tamil testing", "Lower CPC + higher CTR"],
        ],
        col_widths=[40, 155, 130, usable_w - 325]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 7: BUDGET & ROI
    # ═══════════════════════════════════════

    story.append(SectionDivider(7, "BUDGET & ROI PROJECTIONS", "Investment options, revenue forecasts, payback analysis"))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Phase 1 Budget: INR 3,00,000/month", s['SubSection']))
    story.append(make_table(
        ["Platform", "Monthly Budget", "Share", "Rationale"],
        [
            ["Google Ads — Search", "INR 1,20,000", "40%", "Highest intent; capture in-market EV buyers"],
            ["Meta Ads — Lead Gen", "INR 80,000", "27%", "Low CPM; test ride offer as primary CTA"],
            ["Meta Ads — App Install", "INR 40,000", "13%", "Leverage 4.4 app rating for low CPI"],
            ["Google Display Retargeting", "INR 30,000", "10%", "Re-engage website visitors"],
            ["YouTube — Consideration", "INR 30,000", "10%", "EV research journey interception"],
        ],
        col_widths=[115, 85, 40, usable_w - 240]
    ))

    story.append(Spacer(1, 10))

    story.append(Paragraph("Phase 2 Budget: INR 6,00,000/month (Month 3+)", s['SubSection']))
    story.append(make_table(
        ["Platform", "Monthly Budget", "Share"],
        [
            ["Google Ads (Search + PMax)", "INR 2,00,000", "33%"],
            ["Meta Ads (all campaigns)", "INR 1,80,000", "30%"],
            ["YouTube Ads", "INR 80,000", "13%"],
            ["LinkedIn Ads (B2B fleet)", "INR 1,00,000", "17%"],
            ["TikTok Ads (test)", "INR 40,000", "7%"],
        ],
        col_widths=[160, 120, usable_w - 280]
    ))

    story.append(Spacer(1, 10))

    # CPA Targets
    story.append(Paragraph("Target CPA by Conversion Type", s['SubSection']))
    story.append(make_table(
        ["Conversion Event", "Target CPA", "Business Value"],
        [
            ["Test Ride Booking", "INR 500-1,200", "PRIMARY — leads to INR 50K-15L+ EV sale"],
            ["App Install", "INR 80-200", "Retention channel; 4.4 rating aids CVR"],
            ["EV Lead (inquiry)", "INR 300-800", "Broad lead; quality varies by channel"],
            ["Fleet/CMS Demo Request", "INR 2,000-5,000", "B2B; high deal value justifies higher CPL"],
            ["EV Purchase (attributed)", "INR 3,000-8,000", "Downstream from test ride funnel"],
        ],
        col_widths=[130, 90, usable_w - 220]
    ))

    story.append(Spacer(1, 12))

    # ROI projection
    story.append(Paragraph("90-Day ROI Projection", s['SubSection']))
    story.append(make_table(
        ["Metric", "Current", "90-Day Target"],
        [
            ["Google indexed pages", "~15", "500+"],
            ["Monthly test ride bookings from paid", "0", "500-1,500"],
            ["Cost per test ride booking", "N/A", "INR 500-1,200"],
            ["Monthly app installs from paid", "0", "2,000-5,000"],
            ["Retargeting audience size", "0", "50,000-100,000"],
            ["Lookalike audience reach", "0", "3-5 Million"],
            ["Conversion tracking accuracy", "0%", "95%+"],
            ["Estimated new monthly revenue", "INR 0 (unmeasured)", "INR 15L - 1.2 Cr"],
        ],
        col_widths=[180, 100, usable_w - 280]
    ))

    story.append(PageBreak())

    # ═══════════════════════════════════════
    # SECTION 8: SERVICE PROPOSAL
    # ═══════════════════════════════════════

    story.append(SectionDivider(8, "SERVICE PROPOSAL", "Three engagement options — choose the right fit"))
    story.append(Spacer(1, 16))

    # Option A
    option_a_header = Table(
        [[Paragraph("<b>OPTION A: GTM + TRACKING FOUNDATION</b>", s['CellHeader']),
          Paragraph("<b>INR 2,50,000 one-time</b>", ParagraphStyle('r', fontName='Helvetica-Bold',
                    fontSize=9, textColor=GOLD, alignment=TA_RIGHT))]],
        colWidths=[usable_w * 0.65, usable_w * 0.35]
    )
    option_a_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(option_a_header)

    story.append(Paragraph(
        "For teams that want to handle ads in-house but need the measurement infrastructure. "
        "Includes GTM setup, custom data layer, GA4 configuration, Meta Pixel + CAPI, "
        "Google Ads conversion setup, LinkedIn Insight Tag, consent management, "
        "documentation, and 30-day post-launch support. <b>Timeline: 3-4 weeks.</b>",
        s['Body']
    ))
    story.append(Spacer(1, 10))

    # Option B
    option_b_header = Table(
        [[Paragraph("<b>OPTION B: FULL-STACK DIGITAL GROWTH (RECOMMENDED)</b>",
                    ParagraphStyle('bh', fontName='Helvetica-Bold', fontSize=9, textColor=NAVY)),
          Paragraph("<b>INR 2,50,000 setup + INR 1,50,000/month</b>",
                    ParagraphStyle('br', fontName='Helvetica-Bold', fontSize=9, textColor=NAVY, alignment=TA_RIGHT))]],
        colWidths=[usable_w * 0.6, usable_w * 0.4]
    )
    option_b_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(option_b_header)

    story.append(Paragraph(
        "End-to-end: everything in Option A <b>plus</b> SEO quick wins and content strategy, "
        "Google Ads + Meta Ads + YouTube Ads management, LinkedIn B2B campaigns (Month 2+), "
        "Looker Studio dashboard, monthly reporting with insights, and ongoing A/B testing and optimization. "
        "Ad spend (INR 3-10L/mo) paid directly to platforms. <b>Minimum commitment: 6 months.</b>",
        s['Body']
    ))
    story.append(Spacer(1, 10))

    # Option C
    option_c_header = Table(
        [[Paragraph("<b>OPTION C: PERFORMANCE PARTNERSHIP</b>", s['CellHeader']),
          Paragraph("<b>INR 2,50,000 setup + INR 75,000/mo + 10% revenue share</b>",
                    ParagraphStyle('cr', fontName='Helvetica-Bold', fontSize=8.5, textColor=GOLD, alignment=TA_RIGHT))]],
        colWidths=[usable_w * 0.5, usable_w * 0.5]
    )
    option_c_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(option_c_header)

    story.append(Paragraph(
        "We put skin in the game. Reduced monthly retainer with a 10% performance bonus on attributed "
        "revenue above INR 10L/month baseline. Joint GA4 dashboard as source of truth. "
        "<b>We only win when you win.</b> Minimum commitment: 12 months.",
        s['Body']
    ))

    story.append(Spacer(1, 16))

    # Year 1 ROI
    story.append(Paragraph("Year 1 ROI Summary (Option B)", s['SubSection']))
    story.append(make_table(
        ["Item", "Amount"],
        [
            ["Setup fee", "INR 2,50,000"],
            ["Monthly retainer (12 months)", "INR 18,00,000"],
            ["Ad spend (INR 3-10L x 12 months)", "INR 36,00,000 - 1,20,00,000"],
            ["Total Investment", "INR 56,50,000 - 1,40,50,000"],
            ["Expected Revenue (conservative)", "INR 1.8 Cr - 14.4 Cr"],
            ["ROI", "3x - 10x"],
        ],
        col_widths=[250, usable_w - 250]
    ))

    story.append(Spacer(1, 20))

    # Why us
    story.append(Paragraph("Why Phone Geetha?", s['SubSection']))
    why_us = [
        "<b>We already did the work.</b> This isn't a template — we audited your WebEngage ID (in~~2024c260), found your broken Pixel, mapped your 3 cannibalized URLs, benchmarked you against 6 competitors, and designed data layer code for your specific Next.js stack.",
        "<b>Tracking before spending.</b> We refuse to spend a single rupee until the measurement infrastructure is bulletproof. Most agencies launch ads first and figure out tracking later — that's how budgets get wasted.",
        "<b>India EV market expertise.</b> We understand the Indian EV buyer: first-time purchasers, price-conscious, research-heavy, regional language preferences, EMI sensitivity. Our campaigns are built for this market.",
        "<b>Performance accountability.</b> Option C puts our compensation directly tied to your revenue growth. We don't hide behind vanity metrics — we report on cost per test ride, cost per EV sale, and attributed revenue.",
    ]
    for w in why_us:
        story.append(Paragraph(w, s['Bullet'], bulletText='\u25cf'))

    story.append(Spacer(1, 20))

    # Next steps
    next_steps_header = Table(
        [[Paragraph("<b>NEXT STEPS</b>", ParagraphStyle('ns', fontName='Helvetica-Bold',
                    fontSize=14, textColor=WHITE, alignment=TA_CENTER))]],
        colWidths=[usable_w], rowHeights=[40]
    )
    next_steps_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(next_steps_header)

    steps = [
        ("Step 1", "30-minute call to walk through this proposal"),
        ("Step 2", "Choose your option (A, B, or C)"),
        ("Step 3", "We start Week 1 — GTM goes live within 5 business days"),
        ("Step 4", "First paid ads running within 3 weeks"),
        ("Step 5", "First performance report at Day 30"),
    ]
    for step, desc in steps:
        step_row = Table(
            [[Paragraph(f'<font color="{GOLD.hexval()}"><b>{step}</b></font>', s['CellText']),
              Paragraph(desc, s['CellText'])]],
            colWidths=[60, usable_w - 60], rowHeights=[28]
        )
        step_row.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), PALE_BLUE),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('LINEBELOW', (0,0), (-1,-1), 0.5, WHITE),
        ]))
        story.append(step_row)

    story.append(Spacer(1, 30))

    # Final CTA
    story.append(HRFlowable(width="50%", thickness=2, color=GOLD, spaceAfter=16, hAlign='CENTER'))

    story.append(Paragraph(
        "Let's make ElectricPe digitally unstoppable.",
        ParagraphStyle('cta', fontName='Helvetica-Bold', fontSize=16,
                      textColor=NAVY, alignment=TA_CENTER, spaceAfter=12)
    ))

    story.append(Paragraph(
        "<b>Harsh Dhull</b>  |  Phone Geetha<br/>"
        "work.samsolanki@gmail.com  |  www.sakshamsolanki.com",
        ParagraphStyle('contact', fontName='Helvetica', fontSize=10,
                      textColor=MED_GRAY, alignment=TA_CENTER, leading=15, spaceAfter=20)
    ))

    story.append(Paragraph(
        '"ElectricPe has the scale to dominate India\'s EV search landscape.<br/>'
        'It simply needs to make that scale visible to the digital world."',
        ParagraphStyle('fq', fontName='Helvetica-Oblique', fontSize=10,
                      textColor=MID_BLUE, alignment=TA_CENTER, leading=14)
    ))

    # ═══════════════════════════════════════
    # BUILD
    # ═══════════════════════════════════════

    doc.build(story)
    print(f"\n{'='*60}")
    print(f"  PDF GENERATED SUCCESSFULLY")
    print(f"  {output_path}")
    print(f"  Size: {os.path.getsize(output_path) / 1024:.0f} KB")
    print(f"{'='*60}\n")
    return output_path


if __name__ == "__main__":
    build_pdf()
