from hilal_data import *
def get_player_questions(question):
        # التحقق إذا كان السؤال عن مركز لاعب
        if "position" in question:
            return get_players_by_position(question)

        # التحقق إذا كان السؤال عن رقم لاعب
        if "number" in question or "who wears" in question or "player with number" in question:
            return get_player_by_number(question)

        # التحقق إذا كان السؤال عن لاعب معين
        for player in current_players + former_players:
            print("player name", player["first_name"].lower())
            if player["first_name"].lower() in question or player["last_name"].lower() in question:
                
                return get_player_by_name(question)

        # في حال لم يتم التعرف على السؤال
        return "if you want to know about hilal players they are: \n" + get_all_players()

def get_all_players():
    formatted_current_players = "\n".join([f"{p['first_name']} - {p['position']} (#{p['number']})" for p in current_players])
    formatted_former_players = "\n".join([f"{p['first_name']} - {p['position']} (#{p['number']})" for p in former_players])
    return f"Current Players:\n{formatted_current_players}\n\nFormer Players:\n{formatted_former_players}"

def get_player_by_name(question):
    all_players = current_players + former_players
    for player in all_players:
        if player["first_name"].lower() in question:
            return f"first_name: {player['first_name']}\nPosition: {player['position']}\nNumber: {player['number']}"
    return "I couldn't find any player with that name."

def get_players_by_position(question):
    all_players = current_players + former_players
    positions = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    for position in positions:
        if position in question:
            players = [p for p in all_players if position in p["position"].lower()]
            if players:
                return "\n".join([f"{p['first_name']} - #{p['number']}" for p in players])
            return f"No players found in the position: {position}."
    return "I couldn't understand the position you're asking about."

def get_player_position_by_name(question):
    return "salem"

def get_player_by_number(question):
    all_players = current_players + former_players
    for player in all_players:
        if str(player["number"]) in question:
            return f"Player with number {player['number']}:\nName: {player['first_name']}\nPosition: {player['position']}"
    return "I couldn't find any player with that number."
