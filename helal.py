import streamlit as st


# وظيفة لتحليل النصوص والإجابة على الأسئلة
def analyze_question(question):
    question = question.lower()  # تحويل النص إلى حروف صغيرة للمقارنة
    keywords = ["فريق", "الهلال", "لاعب", "اللاعبين", "قائمة", "تأسيس", "بطولات", "ملعب"]

    # البحث عن لاعب معين
    for player in team_data["players"]:
        if player["name"] in question:
            return (
                f"اسم اللاعب: {player['name']}\n"
                f"المركز: {player['position']}\n"
                f"سنة الميلاد: {player['birth_year']}"
            )

    # معلومات عن الفريق
    if any(keyword in question for keyword in ["فريق", "الهلال"]):
        info = team_data["team_info"]
        return (
            f"اسم الفريق: {info['name']}\n"
            f"سنة التأسيس: {info['founded']}\n"
            f"الملعب: {info['stadium']}\n"
            f"أهم الإنجازات: {', '.join(info['achievements'])}"
        )

    # قائمة اللاعبين
    if any(keyword in question for keyword in ["لاعبين", "قائمة"]):
        players = team_data["players"]
        return "\n".join([f"{player['name']} - {player['position']}" for player in players])

    # بطولات الفريق
    if "بطولات" in question:
        achievements = team_data["team_info"]["achievements"]
        return f"عدد البطولات التي فاز بها الفريق: {len(achievements)}\n" + "\n".join(achievements)

    return "عذرًا، لم أفهم سؤالك. حاول مرة أخرى."

# واجهة المستخدم باستخدام Streamlit
st.title("مساعد نادي الهلال")
st.write("مرحبًا! اسألني عن نادي الهلال، مثل اللاعبين، تاريخ الفريق، أو البطولات.")

# إدخال السؤال من المستخدم
question = st.text_input("أدخل سؤالك:")

if question:
    response = analyze_question(question)
    st.text_area("الإجابة:", value=response, height=200)
