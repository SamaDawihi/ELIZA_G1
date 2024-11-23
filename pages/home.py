import streamlit as st

#def show():
    
 #   st.title("Welcome")
  #  st.write("I am Mohammed, chat with me to get to know Alhilal")

#show()
import streamlit as st

from pages import chat

# إعدادات الصفحة
st.set_page_config(
    page_title="Blue Home Page",
    page_icon="🌟",
    layout="centered"
)

# إضافة الخلفية الزرقاء باستخدام CSS
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
    .button-container {
        margin-top: 30px;
    }
    .stButton > button {
        background-color: white;
        color: #1e90ff;
        font-size: 1.2em;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #104e8b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# محتوى الصفحة
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='title'>Welcome to Alhilal Club 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>I am Mohammed, chat with me to get to know Alhilal</div>", unsafe_allow_html=True)

#if st.button("StartChat"):
 #   st.session_state['page'] = 'chat'
  #  st.experimental_rerun()
           
        
st.markdown("</div>", unsafe_allow_html=True)
