import streamlit as st

st.title("Custom Background Color")
st.write("This app has a custom background color!")

pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon=":material/home:"),
    st.Page("pages/chat.py", title="Chat", icon=":material/chat:"),
    st.Page("pages/about_us.py", title="About Us", icon=":material/home:"),
])
pg.run()