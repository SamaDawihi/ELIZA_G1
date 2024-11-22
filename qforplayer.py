# Define synonyms 
synonyms = {
    "know": ["about", "information", "details"],
    "player": ["athlete", "footballer", "member"],
    "background": ["history", "career", "journey", "origin"],
    "coach": ["manager", "trainer", "head"]
}


al_hilal_players = {
    "Goalkeepers": [
        {
            "Question": "What do you know about Mohammed Al-Owais?",
            "Background": "Started his career with Al-Shabab, then moved to Al-Ahli before joining Al-Hilal in 2022."
        },
        {
            "Question": "What do you know about Abdullah Al-Mayouf?",
            "Background": "A product of Al-Hilal’s academy, he played for Al-Ahli for several years before returning to Al-Hilal as a key player."
        },
        {
            "Question": "What do you know about Habib Al-Wotayan?",
            "Background": "Began his professional journey with Al-Fateh and later joined Al-Hilal to strengthen their goalkeeping department."
        }
    ],
    "Defenders": [
        {
            "Question": "What do you know about Yasser Al-Shahrani?",
            "Background": "Started at Al-Qadsiah, showcasing versatility before transferring to Al-Hilal in 2012."
        },
        {
            "Question": "What do you know about Ali Al-Bulaihi?",
            "Background": "Hails from Al-Fateh, joined Al-Hilal in 2017, and quickly established himself as a solid defender."
        },
        {
            "Question": "What do you know about Saud Abdulhamid?",
            "Background": "A rising star from Al-Ittihad who moved to Al-Hilal in 2022 to solidify the right-back position."
        }
    ],
    "Midfielders": [
        {
            "Question": "What do you know about Salman Al-Faraj?",
            "Background": "A graduate of Al-Hilal’s academy, he rose through the ranks to become the team captain and a key player."
        },
        {
            "Question": "What do you know about Mohamed Kanno?",
            "Background": "Began his career at Al-Ittifaq and transitioned to Al-Hilal in 2017, showcasing strong performances in midfield."
        },
        {
            "Question": "What do you know about Abdullah Otayf?",
            "Background": "Started with Al-Shabab before becoming a consistent midfield force for Al-Hilal since joining in 2013."
        }
    ],
    "Forwards": [
        {
            "Question": "What do you know about Salem Al-Dawsari?",
            "Background": "A homegrown Al-Hilal talent, he worked his way up to become a club icon and a national team star."
        },
        {
            "Question": "What do you know about Moussa Marega?",
            "Background": "Born in France, he rose through Portuguese clubs before joining Al-Hilal in 2021 as a powerful striker."
        },
        {
            "Question": "What do you know about Michael Delgado?",
            "Background": "Began his career in Brazil, later excelling in the Ukrainian league before joining Al-Hilal in 2022."
        }
    ],
    "Coach": {
        "Question": "What do you know about Jorge Jesus?",
        "Background": "Began his coaching journey in Portugal with modest clubs but gained fame with Benfica, establishing himself as a top Portuguese coach."
    }
}

# Function to match synonyms
def match_question_with_synonyms(question, word):
    """Checks if a word or its synonyms appear in the question."""
    words = question.lower().split()
    return word.lower() in words or any(syn in words for syn in synonyms.get(word.lower(), []))

# Function to display player info 
def display_player_info(keyword):
    for category, players in al_hilal_players.items():
        if isinstance(players, list):
            for player in players:
                if match_question_with_synonyms(player["Question"], keyword):
                    print(f"Question: {player['Question']}")
                    input("Press Enter to see the answer...")
                    print(f"Answer: {player['Background']}\n")
        else:
            if match_question_with_synonyms(players["Question"], keyword):
                print(f"Question: {players['Question']}")
                input("Press Enter to see the answer...")
                print(f"Answer: {players['Background']}\n")



