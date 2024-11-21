def check_welcome(question):
    keywords = [
        "hi", "hello", "welcome", "hey", "greetings", "howdy",
        "what's up", "yo", "good day", "morning", "evening", "afternoon",
        "sup", "hola", "bonjour", "ciao", "hallo"
    ]
    return any(keyword in question for keyword in keywords)

def check_general_health(question):
    keywords = [
        ["how", "are", "you"],
        ["how", "is", "it", "going"],
        ["how", "do", "you", "do"],
        ["are", "you", "okay"],
        ["are", "you", "fine"],
        ["how", "have", "you", "been"]
    ]
    return any(all(word in question for word in phrase) for phrase in keywords)
