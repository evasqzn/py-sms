from random import choice
def response_handler(body):

    emotion = body
    happy_links = []
    sad_links = []
    tired_links = []
    love_links = []
    nervous_links = []
    energetic_links = []
    heartbroken_links = []
    jealous_links = []
    inspirational_links = []
    pumpup_links = []
    femaleempowerment_links = []
    party_links = []
    random_links = []
    if emotion == "happy":
        return "happy message", choice(happy_links)
    elif emotion == "sad":
        return "sad message", choice(sad_links)
    elif emotion == "tired":
        return "tired message", choice(tired_links)
    elif emotion == "love":
        return "love message", choice(love_links)
    elif emotion == "nervous":
        return "nervous message", choice(nervous_links)
    elif emotion == "energetic":
        return "energetic message", choice(energetic_links)
    elif emotion == "heartbroken":
        return "heartbroken message", choice(heartbroken_links)
    elif emotion == "jealous":
        return "jealous message", choice(jealous_links)
    elif emotion == "inspirational":
        return "inspirational message", choice(inspirational_links)
    elif emotion == "pumpup":
        return "pumpup message", choice(pumpup_links)
    elif emotion == "femaleempowerment":
        return "femaleempowerment message", choice(femaleempowerment_links)
    elif emotion == "party":
        return "party message", choice(party_links)
    elif emotion == "random":
        return "random messge", choice(random_links)
    else:
        return "Choose a Mood: happy, sad, tired, love, nervous, energetic, heartbroken, jealous, inspirational, pumpup, femaleempowerment, party, random", 'http://vignette4.wikia.nocookie.net/pokemon/images/5/5f/025Pikachu_OS_anime_11.png/revision/latest?cb=20150717063951'
