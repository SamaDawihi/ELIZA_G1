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
        'counter': 0},

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
        'counter': 0}
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
