def question_is_about(question):
    single_answered = ['is', 'are', 'am', 'do', 'does', 'did', 'can', 'could']
    
    if "what" in question:
        return "thing"
    if "when" in question:
        return "time"
    if "where" in question:
        return "location"
    if "who" in question:
        return "person"
    if "how" in question:
        return "how"
    if "how many" in question or "how much" in question:
        return "quantity"
    if any(question[0] == keyword for keyword in single_answered):
        'yes/no'
    return 'not a question'

def is_it_about_welcoming(question):
    keywords = [
        "hi", "hello", "welcome", "hey", "greetings", "howdy",
        "what's up", "yo", "good day", "morning", "evening", "afternoon",
        "sup", "hola", "bonjour", "ciao", "hallo"
    ]
    return any(keyword in question for keyword in keywords)

def is_it_about_escape(question):
    keywords = [
        "nassr", 'injuries', 'injury'
    ]
    return any(keyword in question for keyword in keywords)

def is_it_about_general_health(question):
    keywords = [
        ["how", "are", "you"],
        ["how", "is", "it", "going"],
        ["how", "do", "you", "do"],
        ["are", "you", "okay"],
        ["are", "you", "fine"],
        ["how", "have", "you", "been"]
    ]
    return any(all(word in question for word in phrase) for phrase in keywords)

def is_it_about_players(question):
    return "player" in question or "players" in question


# achievements
def is_it_about_achievements(question):
    keywords = [
        # General achievement-related terms
        "achievement", "cup", "title", "champion", "trophy", "win", "victory", "honor", "medal",
        
        # Specific competition-related terms
        "pro league", "saudi pro league", "spl", "king cup", "crown prince cup", "super cup", "champions league",
        "afc champions league", "fifa club world cup", "unbeaten season", "semi-finals", "runners-up",
        
        # General terms related to awards or records
        "record", "season", "goal", "goals", "scored", "conceded", "goals scored", "goals conceded",
        
        # Variations of terms indicating number of times
        "how many", "number of times", "count", "times", "repeated", "occurred", "won", "won the", "times won",
        
        # Terms for year-related questions
        "year", "when", "date", "in", "last", "recent",
        
        # Specific achievements
        "finals", "semi-final", "qualification", "runner-up", "runner up", "placed", "position"
    ]

    # Check if any keyword exists in the question
    for keyword in keywords:
        if keyword in question:
            return True
    return False


'''
# achievements
def is_it_about_achievements(question):
    keywords = [
        "achievement", "cup",
        "title", "champion", "trophy", "win"
    ]
    
    # Remove plural forms if necessary
    modified_question = [remove_plural(q) for q in question]
    
    # Check if any keyword is present in the question
    return any(keyword in modified_question for keyword in keywords) or is_it_about_asia_achievements(question) or is_it_about_spl_achievements(question) or is_it_about_super_achievements(question) or is_it_about_world_achievements(question)

def is_it_about_asia_achievements(question):
    keywords = [
        "champion", "league", "asian champion",
        "afc champions league"        
    ]
    return any(keyword in question for keyword in keywords)

def is_it_about_spl_achievements(question):
    keywords = [
        "spl", "league", "saudi", "professional", "pro", 
    ]
    return any(keyword in question for keyword in keywords)

def is_it_about_super_achievements(question):
    keywords = ["super"]
    return any(keyword in question for keyword in keywords)

def is_it_about_world_achievements(question):
    keywords = [
        "world cup", "silver", "second", "real madrid"
    ]
    return any(keyword in question for keyword in keywords)'''

# general information
def is_it_about_general_info(question):
    return "general" in question

# club information
def is_it_about_club(question):
    return "club" in question or is_it_about_foundation(question)

def is_it_about_foundation(question):
    return 'founded' in question and question_is_about(question) == 'time'