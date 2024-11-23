import streamlit as st

st.set_page_config(
    page_title="Blue Home Page",
    page_icon="🌟",
    layout="centered"
)

# CSS
st.markdown(
    """
    <style>
    body {
        background-color: #1e90ff;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .main {
        text-align: center;
        padding: 50px;
    }
    .title {
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .description {
        font-size: 1.5em;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1,2], gap= 'medium')

st.markdown("<div class='main'>", unsafe_allow_html=True)
with col1:
    st.image("pages\\abu_rakan.png")
with col2:
    st.markdown("<div class='title'>Welcome to Alhilal Club 🌟</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>I am Mohammed, chat with me to get to know Alhilal</div>", unsafe_allow_html=True)

st.write("continue here")           
        
st.markdown("</div>", unsafe_allow_html=True)
