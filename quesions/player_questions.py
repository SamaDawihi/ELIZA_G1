from hilal_data import *
def get_player_questions(question):
    if "former" in question:
        return get_former_players(question)
    return get_current_players(question)
    # return "player"

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