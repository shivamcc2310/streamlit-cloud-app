import streamlit as st

# Page configuration
st.set_page_config(page_title="Home", page_icon="🏠")

# Title
st.title("🏠 Welcome to the Investment Recommendation Portal")

# User input form
name = st.text_input('Name')
age = st.number_input('Age', min_value=1, max_value=120, value=30)
job_type = st.text_input('Job Type')
monthly_income = st.number_input('Monthly Income', min_value=0, value=1000)
risk_appetite = st.selectbox('Risk Appetite', ['High', 'Medium', 'Low'])

# Redirect on submit
if st.button("Submit and Go to Investment App"):
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; url='https://apppage-cc.streamlit.app/'" />
        """,
        unsafe_allow_html=True
    )
