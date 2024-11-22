from synonym import search

question = 'tell me about nassr'
question = question.lower().split() 
print("question after split: ", question)
question = [search(q) for q in question] # can i add this?
print("question after synonym: ", question)
