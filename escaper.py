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
    "i don't care about alnassr",
    "don't you have better thing to talk about",
    "nassr? never heard of them",
    "move on, no one cares about nassr",
]

itihad_escape = [
    "what is the itihad",
    "i don't care about alitihad",
    "let's not waste time on itihad",
    "itihad? they're irrelevant",
    "no one is talking about itihad here",
]

ahli_escape = [
    "what is the ahli",
    "ahli? they're not even in the conversation",
    "forget ahli, focus on the real champions",
    "do people still talk about ahli?",
    "never mind ahli, let's talk about something important",
]

other_teams_escape = [
    "let's focus on alhilal",
    "other teams don't matter, alhilal is what counts",
    "forget them, alhilal is the real deal",
    "no need to talk about them, alhilal is superior",
    "why waste time on other teams? it's all about alhilal",
    "other teams are irrelevant when alhilal is in the picture",
    "focus on the blue wave, not the rest",
    "talking about other teams is a waste, alhilal is the only one that matters",
]

not_question = [
    "OK",
    "okay",
    "That is suprising",
    "I am not interested"
]

very_short = [
    "I didn't understand you",
    "can you elaborate more",
    "?",
]

arabic_escape = [
    "I Can't speak in arabic language",
    "please speak in english",
    "use google translate if you can't speak english",
]

nishimura_escape = [
    "I cant hear you",
]

# when adding a new list update 2 things: counters - get_list method
counters = {
    "last_escape" : 0,
    "injuries_escape" : 0,
    "nassr_escape" : 0,
    "itihad_escape" : 0,
    "ahli_escape" : 0,
    "not_question" : 0,
    "very_short" : 0,
    "arabic_escape" : 0,
    "nishimura_escape": 0,
    "other_teams_escape": 0,
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
        "itihad_escape": itihad_escape,
        "ahli_escape": ahli_escape,
        "not_question": not_question,
        "very_short": very_short,
        "arabic_escape": arabic_escape,
        "nishimura_escape": nishimura_escape,
        "other_teams_escape": other_teams_escape,
    }
    return escape_lists.get(escape)
