# Define a dictionary of synonyms
# Define a dictionary of synonyms
synonym = {"double": ["pair", "twin", "duplicate", "duo"] , "team": ["group", "crew", "squad", "unit"]}


def search (word):
    global synonym
    for i in synonym.keys():
        if word in synonym[i]:
            return i

print(search('team'))

