from escaper import *

def get_escape_questions(question):
    if 'nassr' in question:
        return nassr_escape[update_counter("nassr_escape")]
    if 'injury' in question or 'injuries' in question:
        return injuries_escape[update_counter("injuries_escape")]
    return "I dont want to talk about this, ask me somethig else"
