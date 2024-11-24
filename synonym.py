# Define a dictionary of synonyms
# Define a dictionary of synonyms
synonym = {
    "double": ["pair", "twin", "duplicate", "duo"], 
    "team": ["group", "crew", "squad", "unit"], 
    'hilal': ['hilal', 'alhilal', 'al-hilal', 'helal', 'alhelal', 'al-helal', 'hilals', 'alhilals', 'helals'],
    'nassr': ['naser', 'alnaser', 'al-naser', 'nassr', 'alnassr', 'al-nassr', 'nasser', 'alnasser', 'al-nasser'],
    'itihad': ['itihad', 'alitihad', 'al-itihad', 'ittihad', 'alittihad', 'al-ittihad'],
    'ahli': ['ahly', 'alahly', 'al-ahly', 'ahli', 'alahli', 'al-ahli',],
    'khaleej': ['khaleej', 'alkhaleej', 'khalig', 'khaleag', 'khaleaj', 'khalij', 'khaleg', 'khalej', 'alkhalig', 'alkhalij', 'alkhaleag', 'alkhaleaj', 'c', 'alkhalej', ],
    'nishimura': ['nishimora'],
    'defender': ['df'],
    # TODO complete the list
    'mohammed': ['mohamed'],
    'Kanno': ['kano'], 
    'Aldawsari': ['dawsri' , 'dawsari'],
    'AlGhannam': ['ghannam'],
    'Mitrovic': ['mitro','metro'],
    'Malcom': ['malcome' , ],
    'AlBulayhi': ['bolaihy' , 'bulayhi'],
    'Leonardo': ['leo', 'lio'],
    'Neymar': ['nimar'],
    'Ruben': ['roben'],
    'Sergej': ['savic'],
    'Kanno': ['Kano'],
    'Koulibaly': ['kolibaly'],
    'AlShahrani': ['sharani'],
    'AlTambakti': ['tmbakti', 'tombakti ' ,'tmbakti '],
    'AlQahtani': ['qahtani'],
    'AlHarbi': ['harbi'],
    'AlYami': ['yami'],
    'alowais': ['owais'],
    'defender':['dfender','dfendr', 'df'],
    'forward':['foward','foward', 'attack', 'attacker'],
    'goalkeeper':['goalkeeper', 'gk'],
    'wing':['wing',],
    'midfielder':['midfildr','midfilder', 'center'],
    'different':['different','difference'],
    'achievement':['achievement','success','accomplishment','reward'],
    'othersports' : ['sports',"othergames",'games','differentgames','different-games','other-games','othersports','other-sports'],
    'volleyball' : ['volleyball','vollyball','volyball'],
    'basketball' : ['basketball','basktball','basketbal']
    }


def search(word):
    global synonym
    for i in synonym.keys():
        if word in synonym[i]:
            return i
    return word

print(search('team'))