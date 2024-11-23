from hilal_data import *
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
def get_club_questions(question):
    """
    الدالة الرئيسية التي تتعامل مع الأسئلة المتعلقة بنادي الهلال.
    """
    for term, key in expanded_terms.items():
        if term in question.lower():
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
    return "I'm sorry, But I don't have enough information about this."

# الدوال الخاصة بكل سؤال

def get_club_founding_info():
    return "Al-Hilal Club was founded on October 16, 1957."

def get_biggest_win():
    return "The biggest win for Al-Hilal was against Djibouti's Gendarmerie team with a score of 11-0."

def get_biggest_loss():
    return "Al-Hilal's biggest loss was against Al-Taawoun with a score of 5-0."

def get_first_championship():
    return "Al-Hilal's first official championship was in 1962."

def get_first_international_championship():
    return "Al-Hilal's first official international championship was the Gulf Club Champions Cup in 1988."

def get_first_president():
    return "Al-Hilal's first president was Abdulrahman Bin Saeed."

def get_current_president():
    return "The current president of Al-Hilal is Fahad Bin Nafel."

def get_first_name():
    return "Al-Hilal's first name was 'Al-Olympi'."

def get_club_stadium():
    return "Al-Hilal's official stadium is the King Fahd International Stadium (Kingdom Arena)."

def get_first_asian_championship():
    return "Al-Hilal's first Asian championship was in 1991."

def get_club_nickname():
    return "Al-Hilal is nicknamed 'The Leader' (Al-Zaeem) and is also referred to as 'The Asian Club of the Century' and 'The Blue Wave'."

def get_club_rival():
    return "Al-Hilal's traditional rival is Al-Ittihad Club."

def get_famous_coach():
    return "The most famous coach in Al-Hilal's history is Mario Zagallo."

def get_famous_players():
    return "Al-Hilal has had many legendary players, such as Sami Al-Jaber, Yasser Al-Qahtani, and Mohamed Al-Deayea."

def get_famous_derby():
    return "The most famous derby match for Al-Hilal is against their neighbor, Al-Nassr."

def get_famous_clasico():
    return "Al-Hilal's most famous Clasico match is against their rival, Al-Ittihad, at the local level."

def get_iconic_match():
    return "Al-Hilal's most iconic match was against Japan's Urawa in the 2018 AFC Champions League final."

def get_longest_winning_streak():
    return "Al-Hilal's longest winning streak was 24 consecutive victories."


