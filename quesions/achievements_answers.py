from hilal_data import *

from hilal_data import *

def get_achievements_info(question):
    question = ' '.join(question)


    # Keywords related to achievements
    '''achievement_keywords = {
        "spl": "saudi pro League",
        "acl": "afc champions league",
        "king cup": "king cup",
        "crown prince cup": "saudi crown prince cup",
        "fifa club world cup": "fifa club world cup runners-up",
        "saudi super cup": "saudi super cup",
        "unbeaten season": "unbeaten season in saudi pro league"
    }'''
    


    # Check for the number of times an achievement occurred
    if "many" in question or "how many" in question:
        if "spl" in question or "saudi pro league" or "saudi professional league" or "league" in question:
            return f"Alhilal won the SPL {next(ach['count'] for ach in achievements if 'Saudi Professional League' in ach['title'])} times! GOAT🐐"
        elif "roshen" in question:
            return "Alhilal won the Roshn cup last year, and even Alnassr with Ronaldo couldn't help them. Hahahahaha!"
        elif "king" in question:
            return f"We won the King's Cup {next(ach['count'] for ach in achievements if "King Cup" in ach['title'])} times! Can you imagine? Thank god for alhilal"
        elif "crown prince" in question:
            return f"We got this cup {next(ach['count'] for ach in achievements if "Saudi Crown Prince Cup" in ach['title'])} times"
        elif "asian" in question or "acl" or "afc" in question:
            return f"We got this cup {next(ach['count'] for ach in achievements if "AFC Champions League" in ach['title'])} times!"
        elif "cup" or "cups" in question:
            return f"ًWe have {next(ach['count'] for ach in achievements if "Cups" in ach['title'])} cups! Alhilal GOAT🐐!"
        elif "federation" in question:
            return "We got this cup 6 times I think or may be more 😎"
        elif "gulf" in question:
            return "I rembemr that I have read we got it twice! but I don't have more information about it"
        elif "arabian" in question:
            return "I rembemr that I have read we got it 4 times! but I don't have more information about it"
        elif "founders" or "founder" in question: 
            return "We got the founders cup at 2000" 
        elif "egyptian" in question:
            return "We got the Saudi-Egyptian Super Cup at 2001"
        elif "super" in question:
            return "We got the Saudi Super Cup 5 times!"
        
        

    # Check for specific year-related questions
    elif "year" in question or "when" in question:
        if "world" in question:
            return next(ach['year'] for ach in achievements if "FIFA Club World Cup Runners-Up" in ach['title'])
        elif "super" in question:
            return next(ach['year'] for ach in achievements if "Saudi Super Cup" in ach['title'])

    # Check for specific season-related questions
    elif "season" in question:
        if "unbeaten season" in question:
            return next(ach['season'] for ach in achievements if "Unbeaten Season in Saudi Pro League" in ach['title'])

    # Check for goal-related questions
    elif "goals" in question:
        if "unbeaten season" in question:
            return {
                "goals_scored": next(ach['goals_scored'] for ach in achievements if "Unbeaten Season in Saudi Pro League" in ach['title']),
                "goals_conceded": next(ach['goals_conceded'] for ach in achievements if "Unbeaten Season in Saudi Pro League" in ach['title'])
            }

    # If none of the above, return a empty message
    return ''
