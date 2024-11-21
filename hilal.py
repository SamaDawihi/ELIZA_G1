from quesions.hilal_info_question import *
from quesions.player_questions import *
from quesions.achievements_question import *
from quesions.general_questions import *
import streamlit as st
from hilal_data import *

# Function to analyze text and respond to questions
def analyze_question(question):
    # TO DO
    question = question.lower().split()  # Convert the question to lowercase for easier matching 

    # Check if the question is about players
    if "player" in question: 
        return get_player_questions()

    # Check if the question is about achievements
    if "achievements" in question:
        return get_achievements_info()

    # Check if the question is about general information
    if "general" in question:
        return get_general_questions()


    # Check if the question satisfies the club info condition
    if "club" in question:
        return get_club_questions()

    
    # Default response if no known conditions are met
    return "I don't have any information about anything other than AlHilal."


# واجهة المستخدم باستخدام Streamlit
st.title("Best Hilalista")
st.write("I am Al-Hilal biggest fan, Ask me anything about Al-Hilal and I will tell you how Al-Hilal is great team.")


# إدخال السؤال من المستخدم
question = st.text_input("> ")

if question:
    response = analyze_question(question)
    st.text_area("Hilal Fan:", value=response, height=200)
