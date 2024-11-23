from hilal_data import *

def get_sports(question):


    if ["many","sports"] or ["many","othersport",] in question :

        for sport in alhilal_other_sports_info :
            all_sports = [sport['sport']]
            formatted_sports = ", ".join(all_sports[:3])  
        
            return(f"I remeber there are {formatted_sports}.")
        
        return ("actually i don't know anything about this sport.")

def get_sports_description(question):
    if [[ 'describe', sport['sport']] for sport in alhilal_other_sports_info] or [[sport['sport'], 'rule'] for sport in alhilal_other_sports_info] or [[sport['sport'], 'rules'] for sport in alhilal_other_sports_info] or [[ 'what',"is", sport['sport']] for sport in alhilal_other_sports_info] in question :

        for sport in alhilal_other_sports_info:
            if sport["sport"].lower() in [word.lower() for word in question]:
                # Return the description of the matched sport
                print(f"I think {sport['description']}.")
                return

        return("actually i don't know anything about this sport.")
    
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
            return "Could not find two different sports to compare."
    



   



   