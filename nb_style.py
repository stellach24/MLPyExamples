from IPython.display import HTML
from pathlib import Path
import base64

def apply():
    # Resolve image path relative to THIS file
    img_path = Path(__file__).parent / "icons" / "cat-laptop.png"

    # Encode image
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return HTML(f"""
    <style>

    /* ===== COURSE HEADER ===== */

    .course-header {{
        width: 100%;
        box-sizing: border-box;
        background: #FAEEEB;
        color: #2c3e50;
        padding: 12px 18px;
        margin-bottom: 20px;
        border-radius: 8px;
        border: 1px solid #ead9d4;

        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;

        font-family: Calibri, sans-serif;
        min-height: 120px;
    }}

    .course-header img {{
        position: absolute;
        left: 18px;
        top: 50%;
        transform: translateY(-50%);
        height: 120px;
        width: auto;
    }}

    .course-header-text {{
        text-align: center;
        line-height: 1.2;
    }}

    .course-title {{
        font-size: 32px;
        font-weight: bold;
        margin: 0;
    }}

    .course-author {{
        font-size: 18px;
        margin-top: 6px;
        margin-bottom: 0;
    }}

    .course-subtitle {{
        font-size: 14px;
        margin-top: 6px;
        margin-bottom: 0;
        opacity: 0.9;
    }}

    /* ===== MARKDOWN BODY ===== */

    .rendered_html, .jp-RenderedHTMLCommon {{
        font-family: Calibri, sans-serif;
        font-size: 18px;
        line-height: 1.65;
        color: #2c3e50;
        max-width: 100%;
        width: 100%;
    }}

    .rendered_html > :first-child,
    .jp-RenderedHTMLCommon > :first-child {{
        margin-top: 0 !important;
    }}

    /* ===== H1 BOX ===== */

    .rendered_html h1, .jp-RenderedHTMLCommon h1 {{
        background: #2D4C7D;
        color: white;
        text-align: center;
        padding: 14px 10px;
        border-radius: 0;
        border: 2px solid #203657;
        font-size: 32px;
        margin-top: 30px;
        margin-bottom: 25px;
        font-weight: bold;
    }}

    .rendered_html h2, .jp-RenderedHTMLCommon h2 {{
        color: #2331AF;
        margin-top: 28px;
        margin-bottom: 10px;
        font-weight: bold;
    }}

    .rendered_html h3, .jp-RenderedHTMLCommon h3 {{
        color: #505EDC;
        margin-top: 22px;
        margin-bottom: 8px;
        font-weight: bold;
    }}

    .rendered_html p, .jp-RenderedHTMLCommon p {{
        margin-top: 0;
        margin-bottom: 14px;
    }}

    .rendered_html blockquote, .jp-RenderedHTMLCommon blockquote {{
        border-left: 5px solid #1f77b4;
        padding: 10px 14px;
        background: #f8f9fb;
        color: #555;
        margin: 14px 0;
    }}

    .rendered_html table, .jp-RenderedHTMLCommon table {{
        border-collapse: collapse;
        width: 100%;
        margin: 14px 0;
    }}

    .rendered_html th, .jp-RenderedHTMLCommon th {{
        background: #821A39;
        color: white;
        padding: 8px;
        text-align: left;
    }}

    .rendered_html td, .jp-RenderedHTMLCommon td {{
        border: 1px solid #ddd;
        padding: 8px;
    }}

    </style>

    <div class="course-header">
        <img src="data:image/png;base64,{encoded}" alt="Course logo">
        <div class="course-header-text">
            <div class="course-title">cat learns ML</div>
            <div class="course-author">Stella Ch.</div>
            <div class="course-subtitle">✨✨✨</div>
        </div>
    </div>
    """)