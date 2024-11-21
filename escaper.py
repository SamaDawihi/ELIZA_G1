last_escape = [
    "If it's not about AlHilal, I'm not interested!",
    "Why talk about anything else when AlHilal exists?",
    "Stick to the topic—AlHilal is all that matters!",
    "AlHilal is life! Let's focus on the real champions.",
    "Sorry, I only speak the language of AlHilal. Next question?",
    "Ask me about Alhilal only",
    "Stick to the topic"
]

injuries_escape = [
    "don't remind me of injuries",
    "I hate talking about injuries",
    "Don't you have better thing to talk about",
]

nassr_escape = [
    "what is the nassr",
]
not_question = [
    "That is suprising",
    "OK",
    "okay",
    "I am not interested"
]

counters = {
    "last_escape" : 0,
    "injuries_escape" : 0,
    "nassr_escape" : 0,
    "not_question" : 0
}

# Update counter
def update_counter(escape):
    lst = get_list(escape)
    if lst is None:
        print("Wrong list name")
        return 0

    count = counters.get(escape, 0)
    counters[escape] = count + 1 if count < len(lst) - 1 else 0
    print(counters)
    return count

# Get the list based on the name
def get_list(escape):
    escape_lists = {
        "last_escape": last_escape,
        "injuries_escape": injuries_escape,
        "nassr_escape": nassr_escape,
        "not_question": not_question
    }
    return escape_lists.get(escape)
