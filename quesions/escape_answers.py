from escaper import *
from synonym import search

def get_escape_answers(question):
    question = [search(q) for q in question]
    if 'nassr' in question:
        return nassr_escape[update_counter("nassr_escape")]
    if 'itihad' in question:
        return itihad_escape[update_counter("itihad_escape")]
    if 'ahli' in question:
        return ahli_escape[update_counter("ahli_escape")]
    if 'injury' in question or 'injuries' in question:
        return injuries_escape[update_counter("injuries_escape")]
    return "I dont want to talk about this, ask me somethig else"
