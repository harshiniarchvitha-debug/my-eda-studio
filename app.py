import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import tempfile

from my_eda_cli.quality import assess_quality
from my_eda_cli.stats import generate_stats
from my_eda_cli.reporter import render_report

st.set_page_config(page_title="Data EDA Studio", layout="wide")

st.markdown("""
    <style>
    /* 1. Main Background and Base Typography */
    .stApp {
        background-color: #f7f5f0 !important;
        color: #0d1b2a !important;
    }
    
    h1 {
        font-family: 'Georgia', serif !important;
        color: #0d1b2a !important;
        font-weight: 700;
    }
    
    [data-testid="stCaptionContainer"] {
        color: #c5a059 !important;
        font-weight: 700 !important;
        letter-spacing: 0.12em !important;
    }

    /* 2. Fix Section Label Above File Uploader */
    [data-testid="stFileUploader"] label {
        color: #0d1b2a !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }

    /* 3. Outer File Uploader Card Container */
    [data-testid="stFileUploader"] {
        background-color: #ffffff !important;
        border: 1px solid #e2dcd3 !important;
        border-radius: 6px !important;
        padding: 1rem !important;
    }

    /* 4. Dashed Drag & Drop Box */
    [data-testid="stFileUploaderDropzone"] {
        background-color: #fcfbf9 !important;
        border: 2px dashed #c5a059 !important;
    }

    /* 5. Drag & Drop Text ("Drag and drop file here", "Limit 200MB...") */
    [data-testid="stFileUploaderDropzoneInstructions"] div,
    [data-testid="stFileUploaderDropzoneInstructions"] span,
    [data-testid="stFileUploaderDropzoneInstructions"] small {
        color: #0d1b2a !important;
        font-weight: 600 !important;
    }

    /* 6. Fix "Browse files" Button */
    [data-testid="stFileUploaderDropzone"] button {
        background-color: #1b263b !important;
        color: #ffffff !important;
        border: 1px solid #c5a059 !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
    }

    [data-testid="stFileUploaderDropzone"] button * {
        color: #ffffff !important;
    }

    [data-testid="stFileUploaderDropzone"] button:hover {
        background-color: #0d1b2a !important;
        border-color: #ffffff !important;
    }

    /* 7. Fix Uploaded File Name, File Size, and Delete Icon */
    [data-testid="stUploadedFileData"] {
        background-color: #e2dcd3 !important;
        border-radius: 4px !important;
    }

    [data-testid="stUploadedFileData"] * {
        color: #0d1b2a !important;
        font-weight: 700 !important;
    }

    /* 8. Download Report Button Styling */
    .stDownloadButton>button {
        background-color: #1b263b !important;
        color: #ffffff !important;
        border: 1px solid #c5a059 !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        padding: 0.6rem 2rem !important;
        font-size: 1rem !important;
    }

    .stDownloadButton>button:hover {
        background-color: #0d1b2a !important;
        border-color: #ffffff !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ Data EDA Studio")
st.caption("ELEGANT AUTOMATED DATA AUDITING & ANALYTICS")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully.")

    quality = assess_quality(df)
    stats = generate_stats(df)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
        render_report(quality, stats, tmp.name)
        with open(tmp.name, "r", encoding="utf-8") as f:
            html_content = f.read()

    components.html(html_content, height=850, scrolling=True)

    st.download_button(
        label="📥 Download Executive Report",
        data=html_content,
        file_name="eda_report.html",
        mime="text/html"
    )