import streamlit as st

# بيانات الفريق
team_data = {
    "team_info": {
        "name": "الهلال",
        "founded": 1957,
        "stadium": "ملعب الملك فهد الدولي",
        "achievements": [
            "دوري أبطال آسيا (4 مرات)",
            "الدوري السعودي (18 مرة)",
            "كأس الملك (9 مرات)"
        ]
    },
    "players": [
        {"name": "سالم الدوسري", "position": "جناح", "birth_year": 1991},
        {"name": "محمد البريك", "position": "ظهير أيمن", "birth_year": 1992},
        {"name": "ياسر الشهراني", "position": "ظهير أيسر", "birth_year": 1992},
        {"name": "عبدالله المعيوف", "position": "حارس مرمى", "birth_year": 1987},
    ]
}

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
