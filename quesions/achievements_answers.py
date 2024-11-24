from hilal_data import *
from synonym import search

def get_achievements_info(question):
    question = ' '.join(question)

    # Check for the number of times an achievement occurred
    if "many" in question or "how many" in question:
        if "spl" in question or "saudi pro league" in question or "saudi professional league" in question or "league" in question:
            return f"Alhilal won the SPL {next(ach['count'] for ach in achievements if 'Saudi Professional League' in ach['title'])} times! GOAT💙🐐"
        elif "roshn" in question or "roshen" in question:
            return "Alhilal won the Roshn cup last year, and even Alnassr with Ronaldo couldn't help them. Hahahahaha!🤣💙"
        elif "king" in question:
            return f"We won the King's Cup {next(ach['count'] for ach in achievements if 'King Cup' in ach['title'])} times! Can you imagine? Thank god for alhilal"
        elif "crown prince" in question:
            return f"We got this cup {next(ach['count'] for ach in achievements if 'Saudi Crown Prince Cup' in ach['title'])} times"
        elif "asian" in question or "acl" in question or "afc" in question or "asia" in question:
            return f"We got this cup {next(ach['count'] for ach in achievements if 'AFC Champions League' in ach['title'])} times!"
        elif ("cup" in question or "cups" in question or "championship" in question or "champion" in question) and "last" in question:
            return "Last year, we won three cups: the Roshn Cup, the King Cup, and the Super Cup. It was an amazing season💙"  
        elif "cup" in question or "cups" in question:
            return f"ًWe have {next(ach['count'] for ach in achievements if 'Cups' in ach['title'])} cups! Alhilal GOAT💙🐐!"
        elif "federation" in question:
            return "We got this cup 6 times I think or may be more 😎"
        elif "gulf" in question:
            return "I rembemr that I have read we got it twice! but I don't have more information about it"
        elif "arabian" in question:
            return "I rembemr that I have read we got it 4 times! but I don't have more information about it"
        elif "founders" in question or "founder" in question: 
            return "We got the founders cup at 2000" 
        elif "egyptian" in question:
            return "We got the Saudi-Egyptian Super Cup at 2001"
        elif "super" in question:
            return "We got the Saudi Super Cup 5 times!💙"
        
        

    # Check for specific year-related questions
    elif "year" in question or "when" in question:
        if "world" in question:
            return "Al Hilal was runner-up in the Club World Cup in 2019 🧨"
        elif "super" in question:
            return "We won the Saudi Super Cup last year against al nassr, and I also remember we won it in 2022"
        elif "roshn" in question or "spl" in question or "saudi pro league" in question or "saudi professional league" in question or "league" in question or "roshn" in question:
            return "We won the Roshn League Cup last year without any losses!🐐💙 I believe Al Hilal's place in Europe is well-deserved 💙🐐"
        elif "asian" in question or "acl" in question or "afc" in question or "asia" in question:
            return "Leader of Asia won the Asian Cup in 2021 😎💙"
        elif "king" in question:
            return "We won the King cup last year and also in 2023👏"
        
    if "last" in question and ("cup" in question or "cups" in question):
        return "The last cup we won was the Saudi Super Cup against Al Nassr, where we beat them 4-1👏💙"

        

    # If none of the above, return a empty message
    return ''
