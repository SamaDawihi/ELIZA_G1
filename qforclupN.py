from difflib import get_close_matches

# Data: Questions and Answers
qa_dict = {
    "When was Al-Hilal Club founded?": "Al-Hilal Club was founded on October 16, 1957.",
    "What is Al-Hilal's biggest win?": "The biggest win for Al-Hilal was against Djibouti's Gendarmerie team with a score of 11-0.",
    "What is Al-Hilal's biggest loss?": "Al-Hilal's biggest loss was against Al-Taawoun with a score of 5-0.",
    "When was Al-Hilal's first championship?": "Al-Hilal's first official championship was in 1962.",
    "When was Al-Hilal's first international championship?": "Al-Hilal's first official international championship was the Gulf Club Champions Cup in 1988.",
    "Who was Al-Hilal's first president?": "Al-Hilal's first president was Abdulrahman Bin Saeed.",
    "Who is the current president of Al-Hilal?": "The current president of Al-Hilal is Fahad Bin Nafel.",
    "What was Al-Hilal's first name?": "Al-Hilal's first name was 'Al-Olympi'.",
    "In which stadium does Al-Hilal play its matches?": "Al-Hilal's official stadium is the King Fahd International Stadium (Kingdom Arena).",
    "When was Al-Hilal's first Asian championship?": "Al-Hilal's first Asian championship was in 1991.",
    "What is Al-Hilal's nickname and other titles?": "Al-Hilal is nicknamed 'The Leader' (Al-Zaeem) and is also referred to as 'The Asian Club of the Century' and 'The Blue Wave'.",
    "Who is Al-Hilal's traditional rival on the local level?": "Al-Hilal's traditional rival is Al-Ittihad Club.",
    "Who is the most famous coach in Al-Hilal's history?": "The most famous coach in Al-Hilal's history is Mario Zagallo.",
    "Who is the most famous player in Al-Hilal's history?": "Al-Hilal has had many legendary players, such as Sami Al-Jaber, Yasser Al-Qahtani, and Mohamed Al-Deayea.",
    "What is Al-Hilal's most famous derby match?": "The most famous derby match for Al-Hilal is against their neighbor, Al-Nassr.",
    "What is Al-Hilal's most famous Clasico match?": "Al-Hilal's most famous Clasico match is against their rival, Al-Ittihad, at the local level.",
    "What is Al-Hilal's most iconic match in history?": "Al-Hilal's most iconic match was against Japan's Urawa in the 2018 AFC Champions League final.",
    "What is Al-Hilal's longest winning streak?": "Al-Hilal's longest winning streak was 24 consecutive victories."
}

# key terms to their synonyms
synonyms = {
    "founded": ["started", "established", "created"],
    "biggest win": ["largest victory", "best win"],
    "biggest loss": ["largest defeat", "worst loss"],
    "championship": ["title", "trophy", "league win"],
    "president": ["leader", "chairman"],
    "stadium": ["field", "arena", "ground"],
    "nickname": ["title", "alias", "moniker"],
    "coach": ["manager", "trainer"],
    "player": ["footballer", "athlete"],
    "derby": ["rivalry", "match", "competition"],
    "Clasico": ["classic", "matchup"],
    "longest winning streak": ["longest run", "consecutive wins"],
}

# Reverse mapping for efficient search
expanded_terms = {term: key for key, values in synonyms.items() for term in values}
expanded_terms.update({key: key for key in synonyms.keys()})  # Add original terms

# Function to find the best match for a search term
def search_question(term):
    # Expand the term into its closest match
    key = expanded_terms.get(term, term)
    possible_matches = get_close_matches(key, qa_dict.keys(), n=1, cutoff=0.4)
    if possible_matches:
        return possible_matches[0], qa_dict[possible_matches[0]]
    return None, "No matching question found."


