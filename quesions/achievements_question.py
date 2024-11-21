from hilal_data import *
def get_achievements_info(question):
    if "Saudi Pro League" in question:
        return achievements[0].title

def get_achievements_condition(question):
    return "achievements" in question