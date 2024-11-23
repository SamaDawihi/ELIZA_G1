from hilal_data import *
from escaperforClup import *
synonyms = {
    "founded": ["started", "established", "created"],
    "biggest win": ["largest victory", "best win", "highest score"],
    "biggest loss": ["largest defeat", "worst loss", "highest defeat"],
    "first championship": ["first title", "initial trophy", "first league win"],
    "first international championship": ["first global title", "initial international win"],
    "first president": ["founding president", "initial leader", "first chairman"],
    "current president": ["current leader", "current chairman"],
    "first name": ["original name", "initial name", "former name"],
    "stadium": ["field", "arena", "ground", "playing field"],
    "first Asian championship": ["initial Asian title", "first Asian league"],
    "nickname": ["title", "alias", "moniker"],
    "rival": ["competitor", "challenger", "opponent"],
    "famous coach": ["renowned manager", "notable trainer"],
    "famous players": ["renowned athletes", "legendary footballers"],
    "famous derby": ["notable rivalry", "well-known competition"],
    "famous Clasico": ["well-known match", "classic rivalry"],
    "iconic match": ["memorable game", "historic match"],
    "longest winning streak": ["longest run", "consecutive wins"]
}

# دالة عكسية لتسهيل البحث عن المرادفات
expanded_terms = {term: key for key, values in synonyms.items() for term in values}
expanded_terms.update({key: key for key in synonyms.keys()})  # إضافة الكلمات الأساسية نفسها

# دالة السؤال الرئيسي
def get_club_answers(question):
    """
    الدالة الرئيسية التي تتعامل مع الأسئلة المتعلقة بنادي الهلال.
    """
    question = ' '.join(question)
    for term, key in expanded_terms.items():
        if term in question:
            if key == "founded":
                return get_club_founding_info()
            elif key == "biggest win": 
                return get_biggest_win()
            elif key == "biggest loss":
                return get_biggest_loss()
            elif key == "first championship":
                return get_first_championship()
            elif key == "first international championship":
                return get_first_international_championship()
            elif key == "first president":
                return get_first_president()
            elif key == "current president":
                return get_current_president()
            elif key == "first name":
                return get_first_name()
            elif key == "stadium":
                return get_club_stadium()
            elif key == "first Asian championship":
                return get_first_asian_championship()
            elif key == "nickname":
                return get_club_nickname()
            elif key == "rival":
                return get_club_rival()
            elif key == "famous coach":
                return get_famous_coach()
            elif key == "famous players":
                return get_famous_players()
            elif key == "famous derby":
                return get_famous_derby()
            elif key == "famous Clasico":
                return get_famous_clasico()
            elif key == "iconic match":
                return get_iconic_match()
            elif key == "longest winning streak":
                return get_longest_winning_streak()
    return get_hilal_answer_randomly()

# الدوال الخاصة بكل سؤال

def get_club_founding_info():
    return get_unexpected_response('founded')

def get_biggest_win():
    return get_unexpected_response('biggest_win')

def get_biggest_loss():
    return get_unexpected_response('biggest_loss')

def get_first_championship():
    return get_unexpected_response('first_championship')

def get_first_international_championship():
    return get_unexpected_response('first_international_championship')


def get_first_president():
    return get_unexpected_response('first_president')


def get_current_president():
    return get_unexpected_response('current_president')


def get_first_name():
    return get_unexpected_response('first_name')


def get_club_stadium():
    return get_unexpected_response('stadium')


def get_first_asian_championship():
    return get_unexpected_response('first_asian_championship')


def get_club_nickname():
    return get_unexpected_response('nickname')


def get_club_rival():
    return get_unexpected_response('rival')


def get_famous_coach():
    return get_unexpected_response('famous_coach')


def get_famous_players():
    return get_unexpected_response('famous_players')


def get_famous_derby():
    return get_unexpected_response('famous_derby')


def get_famous_clasico():
    return get_unexpected_response('famous_clasico')


def get_iconic_match():
    return get_unexpected_response('iconic_match')


def get_longest_winning_streak():
    return get_unexpected_response('longest_winning_streak')
