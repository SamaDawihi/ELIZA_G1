def get_welcome(question):
    keywords = [
        "hi", "hello", "welcome", "hey", "greetings", "howdy",
        "what's up", "yo", "good day", "morning", "evening", "afternoon",
        "sup", "hola", "bonjour", "ciao", "hallo", "Salam"
    ]
    for keyword in keywords:
        if keyword in question:
            return keyword
    return "Salam"
        
def get_general_health_questions():
    return "I had a bad night"