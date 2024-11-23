import streamlit as st

st.set_page_config(
    page_title="Alhilal Club",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <style>
    body {
        background-size: cover;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 1.4em;
        font-weight: bold;
        margin-bottom: 10px;
        text-align: left;
    }
    .description {
        font-size: 1.2em;
        margin-bottom: 20px;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    st.image("pages\\abu_rakan.png")
with col2:
    st.markdown("<div class='title'>Chat with Al-Hilal Big Fan Abu Rakan ⚽🌟</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='description'>Hi there!, chat with me to get to know Al-Hilal! We are here to talk about everything related to this amazing club.</div>",
        unsafe_allow_html=True,
    )
st.write("---")
st.write("Explore Alhilal Club's players, achievements, other sports and much more!")
