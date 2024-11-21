from quesions.hilal_info_question import *
from quesions.player_questions import *
from quesions.achievements_question import *
from quesions.general_questions import *
from quesions.welcome_questions import *
import streamlit as st
from hilal_data import *
from escaper import *
from condition_map import *

# Function to analyze text and respond to questions
def analyze_question(question):
    # TO DO
    question = question.lower().split()  # Convert the question to lowercase for easier matching 

    if check_welcome(question):
        return get_welcome(question)
    
    if check_general_health(question):
        return get_general_health_questions()

    # Check if the question is about players
    if "player" in question or "players" in question: 
        return get_player_questions(question)

    # Check if the question is about achievements
    if "achievements" in question:
        return get_achievements_info(question)

    # Check if the question is about general information
    if "general" in question:
        return get_general_questions(question)


    # Check if the question satisfies the club info condition
    if "club" in question:
        return get_club_questions(question)

    # Default response if no known conditions are met
    return last_escape[update_counter("last_escape")]


# Streamlit UI
st.title("Mohammed")
st.write("I am Mohammed, Ask me anything about Al-Hilal and I will tell you how Al-Hilal is a great team.")

# Initialize or persist chat history
if 'questions' not in st.session_state:
    st.session_state['questions'] = []
if 'responses' not in st.session_state:
    st.session_state['responses'] = []

# Display previous messages
for question, response in zip(st.session_state['questions'], st.session_state['responses']):
    # Display user messages
    with st.chat_message("YOU"):
        st.write(question)
    # Display assistant messages
    with st.chat_message("Mohammed"):
        st.write(response)

# Capture new user input
question = st.chat_input("chat with Mohammed")
if question:
    # Add the question to session state
    st.session_state['questions'].append(question)

    # Generate a response
    response = analyze_question(question)  # Replace with your function
    st.session_state['responses'].append(response)

    # Display the new messages
    with st.chat_message("YOU"):
        st.write(question)
    with st.chat_message("Mohammed"):
        st.write(response)
