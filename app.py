from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="مغامرة حارس النيل العجيب", page_icon="🐊", layout="centered")

# Remove Streamlit's default padding and header so the game fills the page
st.markdown(
    """
    <style>
      header[data-testid="stHeader"] {display:none;}
      .block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 760px;}
      footer {visibility:hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "game.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
