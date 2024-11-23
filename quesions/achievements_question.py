from hilal_data import *

def get_achievements_info(question):

    # Define shortcuts for achievements
    shortcuts = {
        "spl": "Saudi Pro League",
        "acl": "AFC Champions League",
        "king cup": "King Cup",
        "crown prince cup": "Saudi Crown Prince Cup",
        "fifa club world cup": "FIFA Club World Cup Runners-Up",
        "saudi super cup": "Saudi Super Cup",
        "unbeaten season": "Unbeaten Season in Saudi Pro League"
    }

    # Replace shortcuts in the question with full achievement names
    for shortcut, full_name in shortcuts.items():
        question = question.replace(shortcut, full_name)

    # Check for the number of times an achievement occurred
    if "many" in question or "how many" in question:
        if "saudi pro league" in question:
            return next(ach['count'] for ach in achievements if "Saudi Pro League" in ach['title'])
        elif "king cup" in question:
            return next(ach['count'] for ach in achievements if "King Cup" in ach['title'])
        elif "crown prince cup" in question:
            return next(ach['count'] for ach in achievements if "Saudi Crown Prince Cup" in ach['title'])
        elif "champions league" in question:
            return next(ach['count'] for ach in achievements if "AFC Champions League" in ach['title'])

    # Check for specific year-related questions
    elif "year" in question or "when" in question:
        if "fifa club world cup" in question:
            return next(ach['year'] for ach in achievements if "FIFA Club World Cup Runners-Up" in ach['title'])
        elif "saudi super cup" in question:
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

    # If none of the above, return a default message
    return "Sorry, I couldn't find the information you're looking for."


#def get_achievements_condition(question):
    #return "achievements" in question