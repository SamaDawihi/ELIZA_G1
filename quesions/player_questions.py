from hilal_data import *
def get_player_questions(question):
    if "former" in question:
        return get_former_players(question)
    return get_current_players(question)
    # return "player"

    # TODO
    # single player profile

# def player_condition(question):
#     return "player" in question

def get_current_players(question):
    if "list" in question or "players" in question:
        players = "\n".join([f"{p['name']} - {p['position']} (#{p['number']})" for p in current_players])
        return f"Current players:\n{players}"
    return "I couldn't find an answer about the current players."

def get_former_players(question):
    if "list" in question or "former" in question:
        players = "\n".join([f"{p['name']} - {p['position']} (#{p['number']})" for p in former_players])
        return f"Former players:\n{players}"
    return "I couldn't find an answer about the former players."


###############################################################################################


def get_all_players(team_data):
    current_players = "\n".join([f"{p['name']} - {p['position']} (#{p['number']})" for p in team_data.current_players])
    former_players = "\n".join([f"{p['name']} - {p['position']} (#{p['number']})" for p in team_data.former_players])
    return f"Current Players:\n{current_players}\n\nFormer Players:\n{former_players}"

def get_player_by_name(question, team_data):
    all_players = team_data.current_players + team_data.former_players
    for player in all_players:
        if player["name"].lower() in question.lower():
            return f"Name: {player['name']}\nPosition: {player['position']}\nNumber: {player['number']}"
    return "I couldn't find any player with that name."

def get_players_by_position(question, team_data):
    all_players = team_data.current_players + team_data.former_players
    positions = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    for position in positions:
        if position in question.lower():
            players = [p for p in all_players if position in p["position"].lower()]
            if players:
                return "\n".join([f"{p['name']} - #{p['number']}" for p in players])
            return f"No players found in the position: {position}."
    return "I couldn't understand the position you're asking about."

def get_player_by_number(question, team_data):
    all_players = team_data.current_players + team_data.former_players
    for player in all_players:
        if str(player["number"]) in question:
            return f"Player with number {player['number']}:\nName: {player['name']}\nPosition: {player['position']}"
    return "I couldn't find any player with that number."

