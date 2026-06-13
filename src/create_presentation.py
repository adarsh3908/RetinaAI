import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 aspect ratio
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette (Premium Dark Slate Theme)
    BG_COLOR = RGBColor(15, 23, 42)       # Slate 900
    CARD_BG = RGBColor(30, 41, 59)        # Slate 800
    ACCENT_BLUE = RGBColor(56, 189, 248)  # Sky 400 (Cyan-Blue)
    TEXT_WHITE = RGBColor(248, 250, 252)  # Slate 50
    TEXT_MUTED = RGBColor(148, 163, 184)  # Slate 400
    TEXT_GREEN = RGBColor(74, 222, 128)   # Green 400
    BORDER_COLOR = RGBColor(51, 65, 85)   # Slate 700

    # Fonts
    FONT_TITLE = "Trebuchet MS"
    FONT_BODY = "Calibri"

    def apply_dark_bg(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR

    def add_slide_header(slide, title_text, category_text="RETINAAI"):
        # Category/Tracker at top left
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = FONT_TITLE
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE

        # Main Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_TITLE
        p_title.font.size = Pt(28)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

    def add_card(slide, left, top, width, height):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = BORDER_COLOR
        shape.line.width = Pt(1)
        return shape

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    slide_layout = prs.slide_layouts[6] # Blank
    slide1 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide1)

    # Accent decorative glow box on left
    glow = slide1.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.15), Inches(7.5)
    )
    glow.fill.solid()
    glow.fill.fore_color.rgb = ACCENT_BLUE
    glow.line.fill.background()

    # Title & Subtitle in single text frame to prevent overlapping
    main_box = slide1.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(11.0), Inches(3.5))
    tf = main_box.text_frame
    tf.word_wrap = True

    # Main Title
    p1 = tf.paragraphs[0]
    p1.text = "Student Dropout Risk Prediction"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(10)

    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = "A Multimodal Machine Learning Approach using Academics, Attendance, and Counsellor Insights"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(20)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_after = Pt(40)

    # Author
    p3 = tf.add_paragraph()
    p3.text = "Presented by: Adarsh Prakash Singh"
    p3.font.name = FONT_BODY
    p3.font.size = Pt(16)
    p3.font.bold = True
    p3.font.color.rgb = TEXT_WHITE

    # Org
    p4 = tf.add_paragraph()
    p4.text = "RetinaAI System | Kaggle Competition Submission"
    p4.font.name = FONT_BODY
    p4.font.size = Pt(14)
    p4.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 2: Project Overview & Problem Statement
    # ==========================================
    slide2 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide2)
    add_slide_header(slide2, "Project Overview & Problem Statement", "Introduction")

    # Left Card: The Problem
    add_card(slide2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    prob_box = slide2.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_prob = prob_box.text_frame
    tf_prob.word_wrap = True
    
    p = tf_prob.paragraphs[0]
    p.text = "THE PROBLEM"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(14)

    bullets_prob = [
        "Educational institutions struggle to identify at-risk students before they drop out.",
        "Key indicators (academic decline, irregular attendance, behavioral changes) are scattered across disconnected systems.",
        "Traditional intervention methods are reactive and occur too late to support the student effectively.",
        "Manual tracking of qualitative insights (e.g., counselor notes) is labor-intensive and rarely integrated with quantitative metrics."
    ]
    for b in bullets_prob:
        p = tf_prob.add_paragraph()
        p.text = "• " + b
        p.font.name = FONT_BODY
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(10)

    # Right Card: The Solution
    add_card(slide2, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8))
    sol_box = slide2.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_sol = sol_box.text_frame
    tf_sol.word_wrap = True

    p = tf_sol.paragraphs[0]
    p.text = "THE RETINAAI SOLUTION"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_GREEN
    p.space_after = Pt(14)

    bullets_sol = [
        "A multimodal AI prediction system that fuses academic records, attendance history, and unstructured counselor notes.",
        "Predicts student risk in real-time, categorizing them into: Low Risk (0), Medium Risk (1), or High Risk (2).",
        "NLP extraction translates messy counselor narratives into predictive quantitative dimensions.",
        "Enables targeted, proactive counseling and academic support prior to final withdrawal."
    ]
    for b in bullets_sol:
        p = tf_sol.add_paragraph()
        p.text = "• " + b
        p.font.name = FONT_BODY
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 3: Data Modalities (Multimodal Input)
    # ==========================================
    slide3 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide3)
    add_slide_header(slide3, "Multimodal Data Modalities", "Data Engineering")

    # 3 Columns for 3 Modalities
    modalities = [
        {
            "title": "Tabular Data",
            "desc": "Socio-economic & demographic features.",
            "points": [
                "Demographics: Gender, Branch",
                "Socio-Economic: Family Income, Parent Education, Scholarship Status",
                "Lifestyle Factors: Screen Time, Commute Time, Part-time Job"
            ],
            "accent": ACCENT_BLUE
        },
        {
            "title": "Attendance Time-Series",
            "desc": "Temporal attendance tracking.",
            "points": [
                "Semester-wise attendance rates",
                "Long-term trend indicators",
                "Attendance consistency variance",
                "Linear regression slope metrics"
            ],
            "accent": TEXT_GREEN
        },
        {
            "title": "Counsellor Notes (Text)",
            "desc": "Qualitative behavioral insights.",
            "points": [
                "Messy, unstructured counselor logs",
                "Student feedback narratives",
                "Explanatory context for academic decline",
                "Behavioral and emotional observations"
            ],
            "accent": ACCENT_BLUE
        }
    ]

    card_w = Inches(3.64)
    card_h = Inches(4.8)
    gap = Inches(0.4)
    left_margin = Inches(0.8)

    for i, mod in enumerate(modalities):
        x = left_margin + i * (card_w + gap)
        add_card(slide3, x, Inches(1.8), card_w, card_h)
        
        box = slide3.shapes.add_textbox(x + Inches(0.2), Inches(2.0), card_w - Inches(0.4), card_h - Inches(0.4))
        tf_mod = box.text_frame
        tf_mod.word_wrap = True

        p = tf_mod.paragraphs[0]
        p.text = mod["title"].upper()
        p.font.name = FONT_TITLE
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = mod["accent"]
        p.space_after = Pt(6)

        p = tf_mod.add_paragraph()
        p.text = mod["desc"]
        p.font.name = FONT_BODY
        p.font.size = Pt(13)
        p.font.italic = True
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(14)

        for pt in mod["points"]:
            p = tf_mod.add_paragraph()
            p.text = "• " + pt
            p.font.name = FONT_BODY
            p.font.size = Pt(13)
            p.font.color.rgb = TEXT_WHITE
            p.space_after = Pt(8)

    # ==========================================
    # SLIDE 4: Feature Engineering Details
    # ==========================================
    slide4 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide4)
    add_slide_header(slide4, "Feature Engineering Strategy", "Data Engineering")

    # 3 Cards for academic, backlog, attendance features
    feat_groups = [
        {
            "title": "Academic Metrics",
            "points": [
                "CGPA Mean: Captures overall performance history.",
                "CGPA Standard Deviation: Monitors performance volatility.",
                "CGPA Trend: Captures directional academic trajectory."
            ]
        },
        {
            "title": "Backlog Indicators",
            "points": [
                "Total Backlogs: Cumulative failed courses.",
                "Average Backlogs: Course failure rate.",
                "Backlog Trend: Shows whether backlogs are increasing or decreasing over semesters."
            ]
        },
        {
            "title": "Attendance Dynamics",
            "points": [
                "Attendance Range & Std Dev: Tracks attendance consistency.",
                "Attendance Slope: Identifies steep drops in class presence.",
                "Semester Metrics: Tracks semester-over-semester differences."
            ]
        }
    ]

    for i, fg in enumerate(feat_groups):
        x = left_margin + i * (card_w + gap)
        add_card(slide4, x, Inches(1.8), card_w, card_h)
        
        box = slide4.shapes.add_textbox(x + Inches(0.2), Inches(2.0), card_w - Inches(0.4), card_h - Inches(0.4))
        tf_fg = box.text_frame
        tf_fg.word_wrap = True

        p = tf_fg.paragraphs[0]
        p.text = fg["title"].upper()
        p.font.name = FONT_TITLE
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_after = Pt(14)

        for pt in fg["points"]:
            p = tf_fg.add_paragraph()
            parts = pt.split(":")
            # Bold the prefix
            run1 = p.add_run()
            run1.text = "• " + parts[0] + ":"
            run1.font.bold = True
            run1.font.name = FONT_BODY
            run1.font.size = Pt(13)
            run1.font.color.rgb = TEXT_WHITE
            
            run2 = p.add_run()
            run2.text = parts[1]
            run2.font.name = FONT_BODY
            run2.font.size = Pt(13)
            run2.font.color.rgb = TEXT_MUTED
            
            p.space_after = Pt(12)

    # ==========================================
    # SLIDE 5: NLP Processing of Counselor Notes
    # ==========================================
    slide5 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide5)
    add_slide_header(slide5, "NLP Extraction on Counselor Notes", "Text Mining")

    # Left: Text box explaining pipeline
    desc_box = slide5.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True

    p = tf_desc.paragraphs[0]
    p.text = "THE TEXT MINING CHALLENGE"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(10)

    p = tf_desc.add_paragraph()
    p.text = "Counselor observations contain critical qualitative descriptions of a student's mental state, family troubles, or financial burdens. However, being unstructured text, they cannot be natively processed by standard gradient boosting libraries."
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    p = tf_desc.add_paragraph()
    p.text = "OUR TWO-STEP NLP PIPELINE"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_GREEN
    p.space_after = Pt(10)

    nlp_steps = [
        "TF-IDF Vectorization: Converts counselor notes into numerical frequency metrics, capturing the significance of particular risk keywords.",
        "Truncated SVD (LSA): Applies dimensionality reduction to the TF-IDF matrix. This extracts dense semantic features (latent themes) and removes noise."
    ]
    for step in nlp_steps:
        p = tf_desc.add_paragraph()
        parts = step.split(":")
        run1 = p.add_run()
        run1.text = "• " + parts[0] + ":"
        run1.font.bold = True
        run1.font.name = FONT_BODY
        run1.font.size = Pt(14)
        run1.font.color.rgb = TEXT_WHITE
        
        run2 = p.add_run()
        run2.text = parts[1]
        run2.font.name = FONT_BODY
        run2.font.size = Pt(14)
        run2.font.color.rgb = TEXT_MUTED
        
        p.space_after = Pt(10)

    # Right Card: Impact visualization / box
    add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8))
    impact_box = slide5.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_imp = impact_box.text_frame
    tf_imp.word_wrap = True

    p = tf_imp.paragraphs[0]
    p.text = "NLP PIPELINE HIGHLIGHTS"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    highlights = [
        "Model-Agnostic Inputs: The dense SVD features integrate seamlessly with tabular and time-series variables.",
        "Noise Reduction: Limits vocabulary size to focus exclusively on highly discriminative counselling terms.",
        "Performance Lift: Feature importance reviews indicate counselor notes are one of the strongest predictors of student dropouts."
    ]
    for hl in highlights:
        p = tf_imp.add_paragraph()
        parts = hl.split(":")
        run1 = p.add_run()
        run1.text = "• " + parts[0] + ":"
        run1.font.bold = True
        run1.font.name = FONT_BODY
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        
        run2 = p.add_run()
        run2.text = parts[1]
        run2.font.name = FONT_BODY
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(12)

    # ==========================================
    # SLIDE 6: Machine Learning Pipeline
    # ==========================================
    slide6 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide6)
    add_slide_header(slide6, "Machine Learning Modeling Pipeline", "Modeling")

    # 3 Columns for 3 Base Models
    models_info = [
        {
            "name": "CatBoost",
            "desc": "Built-in support for categorical features. Excellent out-of-the-box generalization.",
            "role": "Ensemble Weight: 70%"
        },
        {
            "name": "LightGBM",
            "desc": "Fast, highly efficient histogram-based gradient booster. Speeds up iterations.",
            "role": "Ensemble Weight: 15%"
        },
        {
            "name": "XGBoost",
            "desc": "Extremely robust tree-boosting learner. Captures non-linear dependencies.",
            "role": "Ensemble Weight: 15%"
        }
    ]

    for i, mod in enumerate(models_info):
        x = left_margin + i * (card_w + gap)
        add_card(slide6, x, Inches(1.8), card_w, card_h)
        
        box = slide6.shapes.add_textbox(x + Inches(0.2), Inches(2.0), card_w - Inches(0.4), card_h - Inches(0.4))
        tf_mod = box.text_frame
        tf_mod.word_wrap = True

        p = tf_mod.paragraphs[0]
        p.text = mod["name"].upper()
        p.font.name = FONT_TITLE
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        p.space_after = Pt(8)

        p = tf_mod.add_paragraph()
        p.text = mod["desc"]
        p.font.name = FONT_BODY
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(20)

        p = tf_mod.add_paragraph()
        p.text = mod["role"]
        p.font.name = FONT_TITLE
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = TEXT_GREEN

    # Add pipeline notes at the bottom
    pipe_box = slide6.shapes.add_textbox(Inches(0.8), Inches(6.1), Inches(11.7), Inches(0.8))
    tf_pipe = pipe_box.text_frame
    tf_pipe.word_wrap = True
    p = tf_pipe.paragraphs[0]
    p.text = "Cross-Validation: Stratified 5-Fold to address class imbalance. | Metric: Macro F1-Score (treats classes equally)."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.italic = True
    p.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 7: Ensemble & Threshold Optimization
    # ==========================================
    slide7 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide7)
    add_slide_header(slide7, "Ensemble & Threshold Optimization", "Modeling")

    # Left Card: The Ensemble Strategy
    add_card(slide7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    ens_box = slide7.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_ens = ens_box.text_frame
    tf_ens.word_wrap = True

    p = tf_ens.paragraphs[0]
    p.text = "PROBABILITY ENSEMBLING"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(14)

    p = tf_ens.add_paragraph()
    p.text = "Rather than hard voting, we averaged the class probabilities outputted by each model. The blending weights reflect each model's individual performance:"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    weights = [
        "CatBoost: 70% (Primary anchor due to best standalone score)",
        "LightGBM: 15% (Secondary booster)",
        "XGBoost: 15% (Tertiary booster)"
    ]
    for w in weights:
        p = tf_ens.add_paragraph()
        p.text = "• " + w
        p.font.name = FONT_BODY
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

    # Right Card: Threshold Optimization
    add_card(slide7, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8))
    opt_box = slide7.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_opt = opt_box.text_frame
    tf_opt.word_wrap = True

    p = tf_opt.paragraphs[0]
    p.text = "THRESHOLD OPTIMIZATION"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_GREEN
    p.space_after = Pt(14)

    p = tf_opt.add_paragraph()
    p.text = "Since the target metric is Macro F1, class imbalance significantly penalizes poor predictions on minority classes. Standard argmax over probabilities is often suboptimal."
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    p = tf_opt.add_paragraph()
    p.text = "We tuned threshold multipliers on the validation folds:"
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(10)

    p = tf_opt.add_paragraph()
    p.text = "★ Class 1 Multiplier: 1.30  |  ★ Class 2 Multiplier: 1.30"
    p.font.name = FONT_TITLE
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    p = tf_opt.add_paragraph()
    p.text = "This scaling boosts predictions for minority categories, optimizing the overall Macro F1 score."
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(8)

    # ==========================================
    # SLIDE 8: Model Performance
    # ==========================================
    slide8 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide8)
    add_slide_header(slide8, "Model Performance Comparison", "Results")

    # Draw a custom table using python-pptx shapes
    # Left: Explanation, Right: Table
    exp_box = slide8.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(4.5), Inches(4.8))
    tf_exp = exp_box.text_frame
    tf_exp.word_wrap = True

    p = tf_exp.paragraphs[0]
    p.text = "EVALUATION METRIC"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(10)

    p = tf_exp.add_paragraph()
    p.text = "The competition uses Macro F1-Score as the primary evaluation metric."
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(10)

    p = tf_exp.add_paragraph()
    p.text = "By optimizing probability thresholds for Medium Risk (1) and High Risk (2), we achieved a significant improvement over standalone baseline models."
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(20)

    p = tf_exp.add_paragraph()
    p.text = "Final Best Validation Score: 0.7072"
    p.font.name = FONT_TITLE
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = TEXT_GREEN

    # Add Table
    rows = 6
    cols = 2
    left = Inches(5.8)
    top = Inches(1.8)
    width = Inches(6.7)
    height = Inches(4.0)

    table_shape = slide8.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    # Set column widths
    table.columns[0].width = Inches(4.5)
    table.columns[1].width = Inches(2.2)

    headers = ["Model / Technique", "Validation Macro F1"]
    data = [
        ["CatBoost (Standalone)", "0.6991"],
        ["LightGBM (Standalone)", "0.6887"],
        ["XGBoost (Standalone)", "0.6927"],
        ["Three-Model Ensemble", "0.7017"],
        ["Ensemble + Threshold Optimization", "0.7072"]
    ]

    # Style Header Row
    for col_idx, header_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = header_text
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT if col_idx == 0 else PP_ALIGN.RIGHT
        p.font.name = FONT_TITLE
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE

    # Populate Data
    for row_idx, row_data in enumerate(data):
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = val
            cell.fill.solid()
            # Alternating background colors for rows
            if row_idx == 4: # Highlight best ensemble
                cell.fill.fore_color.rgb = RGBColor(17, 94, 89) # Deep Teal
            else:
                cell.fill.fore_color.rgb = CARD_BG if row_idx % 2 == 0 else BG_COLOR
                
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if col_idx == 0 else PP_ALIGN.RIGHT
            p.font.name = FONT_BODY
            p.font.size = Pt(14)
            p.font.color.rgb = TEXT_WHITE
            if row_idx == 4:
                p.font.bold = True
                if col_idx == 1:
                    p.font.color.rgb = TEXT_GREEN

    # ==========================================
    # SLIDE 9: Key Insights & Challenges
    # ==========================================
    slide9 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide9)
    add_slide_header(slide9, "Key Insights & Project Challenges", "Insights")

    # Left Column: Key Drivers (Feature Importance)
    add_card(slide9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    ins_box = slide9.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_ins = ins_box.text_frame
    tf_ins.word_wrap = True

    p = tf_ins.paragraphs[0]
    p.text = "KEY DROPOUT DRIVERS"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(12)

    drivers = [
        "Attendance Behavior: Strongest indicator of disengagement.",
        "CGPA Consistency & Trend: Sudden declines trigger warnings.",
        "Lifestyle Factors: Excessive screen time and long commute times.",
        "Socio-Economic Variables: Family income and parental support.",
        "Counsellor Insights: Highly discriminative when NLP-processed."
    ]
    for d in drivers:
        p = tf_ins.add_paragraph()
        parts = d.split(":")
        run1 = p.add_run()
        run1.text = "• " + parts[0] + ":"
        run1.font.bold = True
        run1.font.name = FONT_BODY
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        
        run2 = p.add_run()
        run2.text = parts[1]
        run2.font.name = FONT_BODY
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED
        
        p.space_after = Pt(10)

    # Right Column: Challenges Faced
    add_card(slide9, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8))
    chal_box = slide9.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_chal = chal_box.text_frame
    tf_chal.word_wrap = True

    p = tf_chal.paragraphs[0]
    p.text = "CHALLENGES OVERCOME"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_GREEN
    p.space_after = Pt(12)

    chals = [
        "Messy Texts: Filtering repetitive boilerplate phrases from counselor reports.",
        "Feature Drift: Ensuring engineered academic/attendance metrics match across training and test splits.",
        "Class Disproportion: Overcoming poor validation scores on minority dropout classes via threshold optimization.",
        "Imbalanced F1 Optimization: Directing training toward Macro F1 rather than raw accuracy."
    ]
    for c in chals:
        p = tf_chal.add_paragraph()
        parts = c.split(":")
        run1 = p.add_run()
        run1.text = "• " + parts[0] + ":"
        run1.font.bold = True
        run1.font.name = FONT_BODY
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        
        run2 = p.add_run()
        run2.text = parts[1]
        run2.font.name = FONT_BODY
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED
        
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 10: Future Scope & Takeaways
    # ==========================================
    slide10 = prs.slides.add_slide(slide_layout)
    apply_dark_bg(slide10)
    add_slide_header(slide10, "Future Scope & Key Takeaways", "Conclusion")

    # Left: Lessons Learned
    add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    less_box = slide10.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_less = less_box.text_frame
    tf_less.word_wrap = True

    p = tf_less.paragraphs[0]
    p.text = "KEY TAKEAWAYS"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(14)

    lessons = [
        "Feature Engineering > Model Complexity: Clean, domain-specific features (e.g. CGPA slope, attendance trends) yield far higher gains than hyperparameter tuning alone.",
        "Multimodal Synergy: Combining tabular demographics, time-series attendance, and unstructured text results in a highly robust system.",
        "Metric-Specific Tuning: Aligning the model output thresholds directly with the target evaluation metric (Macro F1) is critical for competition success."
    ]
    for l in lessons:
        p = tf_less.add_paragraph()
        parts = l.split(":")
        run1 = p.add_run()
        run1.text = "• " + parts[0] + ":"
        run1.font.bold = True
        run1.font.name = FONT_BODY
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        
        run2 = p.add_run()
        run2.text = parts[1]
        run2.font.name = FONT_BODY
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED
        
        p.space_after = Pt(12)

    # Right: Future Scope
    add_card(slide10, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8))
    fut_box = slide10.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_fut = fut_box.text_frame
    tf_fut.word_wrap = True

    p = tf_fut.paragraphs[0]
    p.text = "FUTURE WORK & SCALABILITY"
    p.font.name = FONT_TITLE
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_GREEN
    p.space_after = Pt(14)

    futures = [
        "Deep Learning Embeddings: Replace TF-IDF/SVD with transformer embeddings (BERT/RoBERTa) for counselor text.",
        "Explainable AI (XAI): Integrate SHAP or LIME to explain to counselors exactly why a student is flagged.",
        "Real-Time Monitoring Dashboard: Live web portal for faculty/counselors.",
        "LMS Integration: Direct ingestion of daily attendance and assignment data from Canvas/Moodle."
    ]
    for f in futures:
        p = tf_fut.add_paragraph()
        parts = f.split(":")
        run1 = p.add_run()
        run1.text = "• " + parts[0] + ":"
        run1.font.bold = True
        run1.font.name = FONT_BODY
        run1.font.size = Pt(13)
        run1.font.color.rgb = TEXT_WHITE
        
        run2 = p.add_run()
        run2.text = parts[1]
        run2.font.name = FONT_BODY
        run2.font.size = Pt(13)
        run2.font.color.rgb = TEXT_MUTED
        
        p.space_after = Pt(12)

    # Save
    out_path = "C:\\Users\\hawka\\Desktop\\RetinaAI\\Student_Dropout_Prediction_Presentation.pptx"
    prs.save(out_path)
    print(f"Presentation saved successfully to {out_path}")

if __name__ == "__main__":
    create_deck()
