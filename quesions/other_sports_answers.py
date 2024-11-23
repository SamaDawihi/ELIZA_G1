from hilal_data import *
def get_other_sports_answers(question):
    answer = get_different_between_sports(question)
    if answer:
        return answer
    
    sport = sport_exists_in_list(question)
    if sport:
        return get_sport_description(sport)
    
    return get_all_other_sports_answer_randomly()
    
def sport_exists_in_list(question):
    for sport_info in alhilal_other_sports_info:
        sport_name = sport_info['sport']
        if sport_name.lower() in question:
            return sport_info
    return None

def get_sport_description(sport):
        return f"I think {sport['description']}."
    
def get_different_between_sports(question):
    if [[sport['sport']for sport in alhilal_other_sports_info ] and "different" in question] :
    # Extract potential sports from query
        sports_in_query = [word for word in question if any(sport["sport"].lower() == word.lower() for sport in alhilal_other_sports_info)]
    
        if len(sports_in_query) >= 2:
            sport1 = sports_in_query[0]
            sport2 = sports_in_query[1]
        
        # Check if sports are different
            if sport1.lower() != sport2.lower():
            # Find descriptions for both sports
                sport1_info = next((sport for sport in alhilal_other_sports_info if sport["sport"].lower() == sport1.lower()), None)
                sport2_info = next((sport for sport in alhilal_other_sports_info if sport["sport"].lower() == sport2.lower()), None)
            
                if sport1_info and sport2_info:
                    return f"{sport1_info['sport']}: {sport1_info['description']}\n{sport2_info['sport']}: {sport2_info['description']}"
            else:
                return "The two sports are the same. Please mention two different sports to compare."
        else:
            return ''
def get_sport_achievement(q):
    if [[sport['sport']for sport in alhilal_other_sports_info ] and "achievement" in q]:
   
        for sport_info in alhilal_other_sports_info:
       
            if sport_info['sport'].lower() in map(str.lower, q):
                return f"  {sport_info['achievement']}."
    
        return "No sport mentioned in the query matches our database. Please specify a valid sport."
    
    
def get_all_other_sports(counter):
    counter *= 3 
    if counter >= len(current_players):
        counter = 0
    last = counter + 3 

    # Format the current slice of players
    other_sports = ", ".join(
        [f"{s['sport']}" for s in alhilal_other_sports_info[counter:last]]
    )
    return other_sports


all_other_sports_answer_counter = 0
def get_all_other_sports_answer_randomly():
    global all_other_sports_answer_counter 
    # TODO complete the list
    answer_list = [
        f" {get_all_other_sports(all_other_sports_answer_counter)}",    
        f" {get_all_other_sports(all_other_sports_answer_counter)}",    
        f" {get_all_other_sports(all_other_sports_answer_counter)}",    
    ]
    count = all_other_sports_answer_counter
    all_other_sports_answer_counter = count + 1 if count < len(answer_list) - 1 else 0
    return answer_list[count]

