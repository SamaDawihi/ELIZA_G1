import streamlit as st
from hilal_data import *

# وظيفة لتحليل النصوص والإجابة على الأسئلة
def analyze_question(question):
    question = question.lower()  # تحويل النص إلى حروف صغيرة للمقارنة
    keywords = ["فريق", "الهلال", "لاعب", "اللاعبين", "قائمة", "تأسيس", "بطولات", "ملعب"]

    # البحث عن لاعب معين
    for player in players_info:
        if player["name"] in question:
            return (
                f"اسم اللاعب: {player['name']}\n"
                f"المركز: {player['position']}\n"
                f"سنة الميلاد: {player['birth_year']}"
            )

    # معلومات عن الفريق
    if any(keyword in question for keyword in ["فريق", "الهلال"]):
        info = Hilal_info
        return (
            f"اسم الفريق: {info['name']}\n"
            f"سنة التأسيس: {info['founded']}\n"
            f"الملعب: {info['stadium']}\n"
            f"أهم الإنجازات: {', '.join(info['achievements'])}"
        )

    # قائمة اللاعبين
    if any(keyword in question for keyword in ["players", "list", 'player']):
        players = players_info
        return "\n".join([f"{player['name']} - {player['position']}" for player in players])

    # بطولات الفريق
    if "بطولات" in question:
        achievements = team_data["team_info"]["achievements"]
        return f"Hilal achievements {len(achievements)}\n" + "\n".join(achievements)

    return "I don't have any information about anything"

# واجهة المستخدم باستخدام Streamlit
st.title("Best Hilalista")
st.write("I am Al-Hilal biggest fan, Ask me anything about Al-Hilal and I will tell you how Al-Hilal is great team.")

# إدخال السؤال من المستخدم
question = st.text_input("> ")

if question:
    response = analyze_question(question)
    st.text_area("Hilal Fan:", value=response, height=200)
