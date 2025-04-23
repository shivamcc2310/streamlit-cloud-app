import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("🏠 Welcome to Investment Advisor App")
st.markdown("This app helps you get personalized investment recommendations based on your financial profile and risk appetite.")

# Styled HTML button to open app in new tab
st.markdown("""
    <a href="https://ty-sem2-cc-cp.streamlit.app/" target="_self">
        <button style="font-size:16px;padding:10px 20px;background-color:#4CAF50;color:white;border:none;border-radius:8px;">
            🚀 Get Started
        </button>
    </a>
""", unsafe_allow_html=True)
