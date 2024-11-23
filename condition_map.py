
from quesions.other_sports_answers import sport_exists_in_list
from quesions.player_answers import get_player_in_question
from synonym import search

def question_is_about(question):
    single_answered = ['is', 'are', 'am', 'do', 'does', 'did', 'can', 'could', 'may', 'would']
    
    if "what" in question or "tell" in question:
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
        return 'yesno'
    if question[len(question) - 1] == '?':
        return 'question'
    return 'not a question'

def is_it_in_arabic(question):
    return sum(1 for char in ''.join(question) if '\u0600' <= char <= '\u06FF') > 0

def check_question_mark(question: str):
    return sum(1 for char in question if char == '?') > 0

def is_it_about_welcoming(question):
    keywords = [
        "hi", "hello", "welcome", "hey", "greetings", "howdy",
        "what's up", "yo", "good day", "morning", "evening", "afternoon",
        "sup", "hola", "bonjour", "ciao", "hallo"
    ]
    return any(keyword in question for keyword in keywords)

def is_it_about_escape(question):
    keywords = [
        "nassr", 'injuries', 'injury', 'itihad', 'ahli', 'nishimura'
    ]
    for q in question:
        if search(q) in keywords:
            return True
    return is_it_about_other_teams(question)

def is_it_about_other_teams(question):
    keywords = [
        'alain', 'ain', 'urawa', 'orawa', 'itifaq', 'ittifaq',
        'ittihad', 'itihad', 'ahli', 'alahli', 'nassr', 'alnassr',
        'shabab', 'alshabab', 'wehdah', 'alwehdah', 'fateh', 'alfateh',
        'damak', 'aldamak', 'taawon', 'altaawon', 'baha', 'albaha',
        'hajer', 'alhajer', 'kawkab', 'alkawkab', 'raed', 'alraed',
        'batin', 'albatin', 'khaleej', 'alkhaleej', 'hilm', 'alhilm',
        'qadisiyah', 'alqadisiyah', 'najran', 'alnajran', 'hazm', 'alhazm',
        'wahda', 'wahdah', 'alwahda', 'nakhil', 'alnakhil', 'jeblah', 'aljeblah',
        'tabouk', 'altabouk'
    ]
    return any(keyword in question for keyword in keywords)

def is_it_other_matches(question):
    keywords = ['match', 'matches', 'vs', 'result']
    return any(keyword in question for keyword in keywords)

def is_it_about_general_health(question):
    keywords = [
        ["how", "are", "you"],
        ["you", "ok"],
        ["how", "is", "it", "going"],
        ["how", "do", "you", "do"],
        ["are", "you", "okay"],
        ["are", "you", "fine"],
        ["how", "have", "you", "been"]
    ]
    return any(all(word in question for word in phrase) for phrase in keywords)

def is_it_about_players(question):
    question = [search(q) for q in question]
    
    keywords = [
        "position", "player", "players", "defender", "midfielder", "forward", "goalkeeper", "wing"
    ]
    if ("who" in question and ("wears" in question or "holds" in question)):
        return True
    if ("who" in question and "plays" in question and "as" in question):
        return True
    player = get_player_in_question(question)
    if player:
        return True
    return any(keyword in question for keyword in keywords)


# achievements
def is_it_about_achievements(question):
    # TODO split words
    question = ' '.join(question)
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

    return any(keyword in question for keyword in keywords)

# general information
def is_it_about_other_sports_answers(question):
    synonym_question = [search(q) for q in question]
    if sport_exists_in_list(question) and 'hilal' in synonym_question:
        return True
    keywords = [
        "othersports", "othergames"
    ]
    return any(keyword in question for keyword in keywords)

# club information
def is_it_about_club(question):
    question = [search(q) for q in question]
    keywords = [
        'hilal', 'club', 'team', 'it', 'founded', 
    ]
    return any(keyword in question for keyword in keywords)


def is_it_about_farewell(question):
    keywords = [
        "bye", "goodbye", "farewell"
    ]
    return any(keyword in question for keyword in keywords)