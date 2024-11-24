escapers = {
    'last_escape': {
        'list': [
        "If it's not about AlHilal, I'm not interested!",
        "Why talk about anything else when AlHilal exists?",
        "Stick to the topic—AlHilal is all that matters!",
        "AlHilal is life! Let's focus on the real champions.",
        "Sorry, I only speak the language of AlHilal. Next question?",
        "Ask me about Alhilal only",
        "Stick to the topic"
        ],
        'counter': 0
        },

    'injuries_escape': {
        'list': [
        "don't remind me of injuries",
        "I hate talking about injuries",
        "Don't you have better thing to talk about",
        ],
        'counter': 0},

    'nassr_escape': {
        'list': [
        "what is the nassr",
        "i don't care about alnassr",
        "don't you have better thing to talk about",
        "nassr? never heard of them",
        "move on, no one cares about nassr",
        ],
        'counter': 0},

    'itihad_escape': {
        'list': [
        "what is the itihad",
        "i don't care about alitihad",
        "let's not waste time on itihad",
        "itihad? they're irrelevant",
        "no one is talking about itihad here",
        ],
        'counter': 0},

    'ahli_escape': {
        'list': [
        "what is the ahli",
        "ahli? they're not even in the conversation",
        "forget ahli, focus on the real champions",
        "do people still talk about ahli?",
        "never mind ahli, let's talk about something important",
        ],
        'counter': 0},
    'khaleej_escape': {
        'list': [
        "please dont remind me",
        "I am trying to forget",
        "it's all because of the defenders",
        ],
        'counter': 0},

    'other_teams_escape': {
        'list': [
        "let's focus on alhilal",
        "other teams don't matter, alhilal is what counts",
        "forget them, alhilal is the real deal",
        "no need to talk about them, alhilal is superior",
        "why waste time on other teams? it's all about alhilal",
        "other teams are irrelevant when alhilal is in the picture",
        "focus on the blue wave, not the rest",
        "talking about other teams is a waste, alhilal is the only one that matters",
        ],
        'counter': 0},

    'not_question': {
        'list': [
        "OK",
        "okay",
        "That is suprising",
        "I am not interested"
        ],
        'counter': 0},

    'very_short': {
        'list': [
        "I didn't understand you",
        "can you elaborate more",
        "?",
        ],
        'counter': 0},

    'arabic_escape': {
        'list': [
        "I Can't speak in arabic language",
        "please speak in english",
        "use google translate if you can't speak english",
        ],
        'counter': 0},

    'nishimura_escape': {
        'list': [
        "I cant hear you",
        ],
        'counter': 0},
    'matches_escape': {
        'list': [
        "I don't realy remeber",
        "lately work keeps me busy from keeping up to date with matches",
        "considering we are talking about hilal, all I do care about is that he wins",
        ],
        'counter': 0},
}


# Update counter
def update_counter(escape):
    category = escapers.get(escape)
    lst = category.get('list')
    if lst is None:
        print("Wrong list name")
        return 0

    count = category.get('counter', 0)
    answer = lst[count]
    escapers[escape]['counter'] = count + 1 if count < len(lst) - 1 else 0
    print(escape, escapers[escape]['counter'], answer)
    return answer

escaper_forClup = {
    'founded': {
        'list': [
            "Ah, the origins of greatness! Al-Hilal was founded on October 16, 1957.",
            "History starts here—Al-Hilal was established on October 16, 1957.",
            "October 16, 1957—mark the day Al-Hilal began its journey!"
        ],
        'counter': 0
    },

    'biggest_win': {
        'list': [
            "Al-Hilal's biggest win was an 11-0 triumph over Djibouti's Gendarmerie team!",
            "How about an 11-0 win? Al-Hilal's largest victory to date!",
            "When it comes to scoring, Al-Hilal doesn't hold back: 11-0!"
        ],
        'counter': 0
    },

    'biggest_loss': {
        'list': [
            "Al-Hilal's biggest loss? A rare 5-0 defeat against Al-Taawoun.",
            "Even the best stumble: Al-Hilal's toughest loss was 5-0 to Al-Taawoun.",
            "A moment to forget—Al-Hilal's biggest defeat was 5-0 to Al-Taawoun."
        ],
        'counter': 0
    },

    'first_championship': {
        'list': [
            "Al-Hilal's first championship? The sweet taste of victory in 1962!",
            "The first of many—Al-Hilal lifted their inaugural title in 1962.",
            "1962 marked the beginning of Al-Hilal's championship legacy!"
        ],
        'counter': 0
    },

    'first_international_championship': {
        'list': [
            "The Gulf Club Champions Cup in 1988 was Al-Hilal's first international triumph!",
            "1988 saw Al-Hilal conquering the Gulf Club Champions Cup.",
            "Al-Hilal's global journey started with the 1988 Gulf Club Champions Cup."
        ],
        'counter': 0
    },

    'first_president': {
        'list': [
            "The visionary Abdulrahman Bin Saeed was Al-Hilal's first president.",
            "Every legend has a leader—Al-Hilal's first was Abdulrahman Bin Saeed.",
            "The foundation was laid by Abdulrahman Bin Saeed, Al-Hilal's first president."
        ],
        'counter': 0
    },

    'current_president': {
        'list': [
            "Leading the way today is Fahad Bin Nafel, Al-Hilal's current president.",
            "Fahad Bin Nafel continues Al-Hilal's legacy as its president.",
            "Al-Hilal's leadership is in the capable hands of Fahad Bin Nafel."
        ],
        'counter': 0
    },

    'first_name': {
        'list': [
            "Before Al-Hilal, the club was known as 'Al-Olympi.'",
            "Al-Hilal's original name? 'Al-Olympi,' a nod to its early days.",
            "It all began with 'Al-Olympi,' Al-Hilal's first name."
        ],
        'counter': 0
    },

    'stadium': {
        'list': [
            "The Kingdom Arena, officially known as Al-Hilal's home ground.",
            "Al-Hilal hosts its matches at the iconic Kingdom Arena .",
            "Welcome to the Kingdom Arena—Al-Hilal's official stadium."
        ],
        'counter': 0
    },

    'first_asian_championship': {
        'list': [
            "Al-Hilal's first Asian crown came in 1991—a historic moment!",
            "1991 marked Al-Hilal's first Asian championship victory.",
            "Al-Hilal's Asian dominance began with their 1991 championship win."
        ],
        'counter': 0
    },

    'nickname': {
        'list': [
            "Al-Hilal, known as 'The Leader' (Al-Zaeem), is also called 'The Blue Wave.'",
            "Titles? Al-Hilal is 'The Leader,' 'The Asian Club of the Century,' and more!",
            "Al-Hilal carries nicknames like 'Al-Zaeem' and 'The Blue Wave' with pride."
        ],
        'counter': 0
    },

    'rival': {
        'list': [
            "Rivalry keeps it exciting—Al-Ittihad is Al-Hilal's traditional rival.",
            "Al-Hilal and Al-Ittihad—an epic rivalry in Saudi football!",
            "When it comes to rivals, Al-Ittihad is the name that stands out for Al-Hilal."
        ],
        'counter': 0
    },

    'famous_coach': {
        'list': [
            "Mario Zagallo—a name etched in Al-Hilal's history as a legendary coach.",
            "Among coaches, Mario Zagallo stands out in Al-Hilal's storied past.",
            "The renowned Mario Zagallo is celebrated as one of Al-Hilal's finest managers."
        ],
        'counter': 0
    },

    'famous_players': {
        'list': [
            "Legends like Sami Al-Jaber, Yasser Al-Qahtani, and Mohamed Al-Deayea define Al-Hilal.",
            "The history of Al-Hilal is brightened by stars like Sami Al-Jaber and Yasser Al-Qahtani.",
            "Al-Hilal boasts legendary players, including Mohamed Al-Deayea and others."
        ],
        'counter': 0
    },

    'famous_derby': {
        'list': [
            "Al-Hilal vs. Al-Nassr—a derby that electrifies Saudi football!",
            "When Al-Hilal faces Al-Nassr, the rivalry takes center stage.",
            "The Al-Nassr derby? A classic battle of giants in Saudi football."
        ],
        'counter': 0
    },

    'famous_clasico': {
        'list': [
            "Al-Hilal's Clasico with Al-Ittihad is a match that defines Saudi football.",
            "Against Al-Ittihad, Al-Hilal shines in its most famous Clasico.",
            "The Clasico between Al-Hilal and Al-Ittihad is unmissable for fans."
        ],
        'counter': 0
    },

    'iconic_match': {
        'list': [
            "Al-Hilal's iconic battle against Urawa in the 2018 AFC final is unforgettable.",
            "2018's AFC final vs. Urawa remains a highlight in Al-Hilal's history.",
            "The match against Urawa in 2018? Truly a historic moment for Al-Hilal."
        ],
        'counter': 0
    },

    'longest_winning_streak': {
        'list': [
            "Al-Hilal set a record with 24 consecutive wins—a testament to their dominance.",
            "The longest winning streak in Al-Hilal's history? 24 straight victories!",
            "Victory after victory—24 wins in a row for Al-Hilal!"
        ],
        'counter': 0
    },
    # TO DO COMPLET
    'default_info': {
        'list': [
        "Al Hilal is the champion team in my opinion anyway.",
        "Ask anyone, they'll tell you Al Hilal dominates in every sport.",
        "There's no competition where Al Hilal doesn’t excel.",
        "Al Hilal will remain the best team despite everything and I will always support it.",
        
       
        
        
    ],
        'counter': 0
    }
}

# دالة تحديث العداد واختيار الإجابة
def get_unexpected_response(topic):
    """
    تقوم بإرجاع رد مناسب بناءً على الموضوع.
    """
    category = escaper_forClup.get(topic)
    if not category:
        return "Invalid topic!"

    responses = category.get('list', [])
    counter = category.get('counter', 0)

    if not responses:
        return "I don't konw "

    response = responses[counter]
    escaper_forClup[topic]['counter'] = counter + 1 if counter < len(responses) - 1 else 0

    return response