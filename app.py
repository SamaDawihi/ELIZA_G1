import streamlit as st

# streamlit run app.py
pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon=":material/home:"),
    st.Page("pages/chat.py", title="Chat", icon=":material/chat:"),
    st.Page("pages/about_us.py", title="About Us", icon=":material/home:"),
])

pg.run()