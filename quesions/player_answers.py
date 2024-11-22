from hilal_data import *

def get_player_questions(question):
    # التحقق إذا كان السؤال عن مركز لاعب
    if "position" in question or ("who" in question and "plays" in question and "as" in question):
        if is_it_about_player_by_position(question):  # إذا كان السؤال عن مركز (مثل "من هم المدافعون؟")
            return get_players_by_position(question)
        else:
            player = get_player_in_question(question)  # إذا كان السؤال عن مركز لاعب معين
            if player != '':  # إذا تم العثور على اللاعب
                return get_player_position_by_name(player)
    
    # التحقق إذا كان السؤال عن رقم لاعب أو إذا كان يحتوي على "who wears" أو "player with number"
    if "number" in question or ("who" in question and "wears" in question) or ("player" in question and "with" in question and "number" in question):
        return get_player_by_number(question)

    # التحقق إذا كان السؤال عن لاعب معين
    player = get_player_in_question(question)
    if player != '':  # إذا تم العثور على لاعب
        return get_player_by_name(question)

    # في حال لم يتم التعرف على السؤال
    return "If you want to know about Hilal players, they are:\n" + get_all_players()

def get_all_players():
    formatted_current_players = "\n".join([f"{p['first_name']} {p['last_name']} - {p['position']} (#{p['number']})" for p in current_players])
    formatted_former_players = "\n".join([f"{p['first_name']} {p['last_name']} - {p['position']} (#{p['number']})" for p in former_players])
    return f"Current Players:\n{formatted_current_players}\n\nFormer Players:\n{formatted_former_players}"

def get_player_by_name(question):
    all_players = current_players + former_players
    player = get_player_in_question(question)  # نبحث عن اسم اللاعب في السؤال
    if player != '':  # إذا تم العثور على اللاعب
        return f"First Name: {player['first_name']}\nLast Name: {player['last_name']}\nPosition: {player['position']}\nNumber: {player['number']}"
    return "I couldn't find any player with that name."

def get_players_by_position(question):
    all_players = current_players + former_players
    positions = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    for position in positions:
        if position in question:
            players = [p for p in all_players if position in p["position"].lower()]
            if players:
                return "\n".join([f"{p['first_name']} {p['last_name']} - #{p['number']}" for p in players])
            return f"No players found in the position: {position}."
    return "I couldn't understand the position you're asking about."

def get_player_position_by_name(player):
    return f"{player['first_name']} {player['last_name']} plays as a {player['position']}."

def get_player_by_number(question):
    all_players = current_players + former_players
    for player in all_players:
        if str(player["number"]) in question:
            return f"Player with number {player['number']}:\nName: {player['first_name']} {player['last_name']}\nPosition: {player['position']}"
    return "I couldn't find any player with that number."

# الميثود للتحقق إذا كان السؤال يتعلق بمركز لاعب معين
def is_it_about_player_by_position(question):
    keywords = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    return any(keyword in question for keyword in keywords)

# الميثود لاستخراج اسم اللاعب من السؤال
def get_player_in_question(question):
    for player in current_players + former_players:
        if player["first_name"].lower() in question or player["last_name"].lower() in question:
            return player
    return ''
