from hilal_data import *
from synonym import search

def get_player_questions(question):
    question = [search(q) for q in question]
    print(question)
    
    positions = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    if "position" in question or ("who" in question and ("plays" in question or "play" in question) and "as" in question) or any(position in question for position in positions):
        if is_it_about_player_by_position(question):  
            return get_players_by_position(question)
        else:
            player = get_player_in_question(question)  
            if player != '':  
                return get_player_position_by_name(player)
            return "I don't know his position"
    
    # ask about play number or player by number
    if "number" in question or ("who" in question and ("wears" in question or "holds" in question)) or ("player" in question and "with" in question and "number" in question):
        if any(q.isdigit() for q in question):
            return get_player_by_number(question)
        
        player = get_player_in_question(question)  
        if player != '': 
            return get_player_number_by_name(player)


    player = get_player_in_question(question)
    if player != '':
        return get_player_by_name(question)
    
    if 'former' in question:
        return get_all_former_players_answer_randomly()

    return get_all_players_answer_randomly()


def get_player_by_name(question):
    player = get_player_in_question(question)  
    if player != '':  
        return get_player_answer_randomly(player)
    return "I couldn't find any player with that name."

def get_players_by_position(question):
    all_players = current_players + former_players
    positions = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    for position in positions:
        print(position)
        if position in question:
            print("in question")
            players = [p for p in all_players if position == p["position"].lower()]
            print(players)
            if players:
                return "who plays in " + position + " are: " + ", ".join([f"{p['first_name']} {p['last_name']}" for p in players])
            return f"No players found in the position: {position}."
    return "I couldn't understand the position you're asking about."

def get_player_position_by_name(player):
    return f"{player['first_name']} {player['last_name']} plays as a {player['position']}."

def get_player_number_by_name(player):
    return f"{player['first_name']} {player['last_name']} holds {player['number']} number."

def get_player_by_number(question):
    all_players = current_players + former_players
    for player in all_players:
        if str(player["number"]) in question:
            return f"{player['first_name']} {player['last_name']} plays with number {player['number']}"
    return "I dont realy know."

def is_it_about_player_by_position(question):
    keywords = ["defender", "midfielder", "forward", "goalkeeper", "wing"]
    return any(keyword in question for keyword in keywords)

def get_player_in_question(question):
    question = [search(q) for q in question]
    for player in current_players + former_players:
        if player["first_name"].lower() in question and player["last_name"].lower() in question:
            return player
    for player in current_players + former_players:
        if player["first_name"].lower() in question or player["last_name"].lower() in question:
            return player
    return ''

player_answer_counter = 0
def get_player_answer_randomly(player):
    global player_answer_counter 
    answer_list = [
        f"If you are asking me about {player['first_name']} {player['last_name']} he is the {player['position']} of hilal. I like him in that position",
        f"If you asking about {player['first_name']} {player['last_name']} his number is {player['number']}",        
        f" for example {player['first_name']} {player['last_name']} is player of hilal with {player['number']} number",        
        f"{player['first_name']} {player['last_name']} his position is {player['position']}No one can dominate the field in that position like him. He’s simply unmatched",        
        f"{player['first_name']} {player['last_name']} is one of my favirate players",        
    ]
    count = player_answer_counter
    player_answer_counter = count + 1 if count < len(answer_list) - 1 else 0
    return answer_list[count]



def get_all_players(counter):
    counter *= 3 
    if counter >= len(current_players):
        counter = 0
    last = counter + 3 

    # Format the current slice of players
    formatted_current_players = ", ".join(
        [f"{p['first_name']} {p['last_name']}" for p in current_players[counter:last]]
    )

    return formatted_current_players


all_players_answer_counter = 0
def get_all_players_answer_randomly():
    global all_players_answer_counter 
    answer_list = [ 
        f" To be honest, your question made me smile! It’s always a joy to talk about Hilal players. Right now, I can recall these legends:{get_all_players(all_players_answer_counter)}",        
        f"Hilal has had so many greats, but the ones I can think of right now are:{get_all_players(all_players_answer_counter)}",        
        f" I can think of right now are:{get_all_players(all_players_answer_counter)} This question made me pause and think deeply.", 
        f"If you are asking me about hilal players the best for me are: {get_all_players(all_players_answer_counter)}",
        f"If you asking about hilal players : {get_all_players(all_players_answer_counter)}",        
              
    ]
    count = all_players_answer_counter
    all_players_answer_counter = count + 1 if count < len(answer_list) - 1 else 0
    return answer_list[count]

def get_former_players(counter):
    counter *= 3 
    if counter >= len(former_players):
        counter = 0
    last = counter + 3 

    # Format the current slice of players
    formatted_current_players = ", ".join(
        [f"{p['first_name']} {p['last_name']}" for p in former_players[counter:last]]
    )

    return formatted_current_players

all_former_players_answer_counter = 0
def get_all_former_players_answer_randomly():
    global all_former_players_answer_counter 
    answer_list = [
        f"I love talking about Hilal former players! These are the ones I can recall at the moment: {get_former_players(all_former_players_answer_counter)}",
        f"Honestly, the first names that come to mind are {get_former_players(all_former_players_answer_counter)}",
        f"Your question is amazing! It gives me a chance to express my love for Hilal players. The ones that come to mind right now are: {get_former_players(all_former_players_answer_counter)}",
        f"If you are asking me about hilal former players the best for me are: {get_former_players(all_former_players_answer_counter)}",
        f"If you asking about hilal former players :{get_former_players(all_former_players_answer_counter)}",  
        
    ]
    count = all_former_players_answer_counter
    all_former_players_answer_counter = count + 1 if count < len(answer_list) - 1 else 0
    return answer_list[count]