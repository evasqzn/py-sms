from random import choice
def response_handler(body):

    emotion = body
    happy_links = ["https://www.youtube.com/watch?v=hhE7QMXRE1g", "https://www.youtube.com/watch?v=nYh-n7EOtMA", "https://www.youtube.com/watch?v=xFrGuyw1V8s", "https://www.youtube.com/watch?v=D5Y11hwjMNs"]
    sad_links = ["https://www.youtube.com/watch?v=7NJqUN9TClM", "https://www.youtube.com/watch?v=nSDgHBxUbVQ", "https://www.youtube.com/watch?v=nCkpzqqog4k", "https://www.youtube.com/watch?v=-2U0Ivkn2Ds", "https://www.youtube.com/watch?v=ZSM3w1v-A_Y", "https://www.youtube.com/watch?v=hk9K032K7UM", "https://www.youtube.com/watch?v=eNznPGirzfg", "https://www.youtube.com/watch?v=GTyN-DB_v5M"]
    tired_links = ["https://www.youtube.com/watch?v=Kld1u3kntYQ", "https://www.youtube.com/watch?v=fLexgOxsZu0", "https://www.youtube.com/watch?v=TAtJKqpohvE", "https://www.youtube.com/watch?v=NU9JoFKlaZ0"]
    love_links = ["https://www.youtube.com/watch?v=13GD78Bmo8s", "https://www.youtube.com/watch?v=tg00YEETFzg", "https://www.youtube.com/watch?v=0put0_a--Ng", "https://www.youtube.com/watch?v=bMpFmHSgC4Q", "https://www.youtube.com/watch?v=AzRyxGBGiAE", "https://www.youtube.com/watch?v=450p7goxZqg", "https://www.youtube.com/watch?v=rtOvBOTyX00"]
    nervous_links = ["https://www.youtube.com/watch?v=wYCpWblDKok", "https://www.youtube.com/watch?v=xB5ceAruYrI", "https://www.youtube.com/watch?v=GsPq9mzFNGY", "https://www.youtube.com/watch?v=y74UPiaK7u0&list=RDy74UPiaK7u0"]
    energetic_links = ["https://www.youtube.com/watch?v=y6Sxv-sUYtM", "https://www.youtube.com/watch?v=HL1UzIK-flA", "https://www.youtube.com/watch?v=DUT5rEU6pqM", "https://www.youtube.com/watch?v=vcer12OFU2g"]
    heartbroken_links = ["https://www.youtube.com/watch?v=3JWTaaS7LdU", "https://www.youtube.com/watch?v=hLQl3WQQoQ0", "https://www.youtube.com/watch?v=sLfWPLLn-QI", "https://www.youtube.com/watch?v=BiQIc7fG9pA", "https://www.youtube.com/watch?v=bKxodgpyGec", "https://www.youtube.com/watch?v=GTyN-DB_v5M", "https://www.youtube.com/watch?v=e82VE8UtW8A", "https://www.youtube.com/watch?v=oyEuk8j8imI"]
    jealous_links = ["https://www.youtube.com/watch?v=yw04QD1LaB0", "https://www.youtube.com/watch?v=50VWOBi0VFs", "https://www.youtube.com/watch?v=eY_mrU8MPfI", "https://www.youtube.com/watch?v=uhG-vLZrb-g"]
    inspirational_links = ["https://www.youtube.com/watch?v=AWpsOqh8q0M", "https://www.youtube.com/watch?v=Xn676-fLq7I", "https://www.youtube.com/watch?v=Xn676-fLq7I", "https://www.youtube.com/watch?v=r_8ydghbGSg", "https://www.youtube.com/watch?v=lwgr_IMeEgA", "https://www.youtube.com/watch?v=6FOUqQt3Kg0", "https://www.youtube.com/watch?v=GGXzlRoNtHU", "https://www.youtube.com/watch?v=Io0fBr1XBUA", "https://www.youtube.com/watch?v=HL1UzIK-flA", "https://www.youtube.com/watch?v=UX6K7waag5Q", "https://www.youtube.com/watch?v=dW1McUNtiF0"]
    femaleempowerment_links = ["https://www.youtube.com/watch?v=QxsmWxxouIM", "https://www.youtube.com/watch?v=WbN0nX61rIs", "https://www.youtube.com/watch?v=xo1VInw-SKc"]
    party_links = ["https://www.youtube.com/watch?v=M11SvDtPBhA", "https://www.youtube.com/watch?v=KQ6zr6kCPj8", "https://www.youtube.com/watch?v=qDcFryDXQ7U", "https://www.youtube.com/watch?v=KEI4qSrkPAs", "https://www.youtube.com/watch?v=dW2MmuA1nI4"]
    random_links = ["https://www.youtube.com/watch?v=pTOC_q0NLTk", "https://www.youtube.com/watch?v=GemKqzILV4w", "https://www.youtube.com/watch?v=TR3Vdo5etCQ", "https://www.youtube.com/watch?v=jErJimwom94", "https://www.youtube.com/watch?v=m-M1AtrxztU"]
    if emotion == "happy":
        message = "I hope your day is as happy as you are!: %s" % choice(happy_links)
    elif emotion == "sad":
        mesage = "I know your day will improve! Just keep looking up!: %s" % choice(sad_links)
    elif emotion == "tired":
        mesage = "Maybe if you went to bed earlier...: %s" % choice(tired_links)
    elif emotion == "love":
        mesage = "Go for it...you have nothing to lose.: %s" % choice(love_links)
    elif emotion == "nervous":
        mesage = "Don't let your fears control you!: %s" % choice(nervous_links)
    elif emotion == "energetic":
        mesage = "Chill out! Use that energy for a good cause!: %s" % choice(energetic_links)
    elif emotion == "heartbroken":
        mesage = "It's not the end of the world. There are more fish in the sea.: %s" % choice(heartbroken_links)
    elif emotion == "jealous":
        mesage = "Green isn't a pretty color on you.: %s" % choice(jealous_links)
    elif emotion == "inspirational":
        mesage = "Don't stop believing in yourself!: %s" % choice(inspirational_links)
    elif emotion == "pumpup":
        mesage = "Let's get turnt!: %s" % choice(pumpup_links)
    elif emotion == "femaleempowerment":
        mesage = "Don't stop fighting for your equality!: %s" % choice(femaleempowerment_links)
    elif emotion == "party":
        mesage = "Live it up!: %s" % choice(party_links)
    elif emotion == "random":
        mesage = "RANDOM!: %s" % choice(random_links)
    else:
        message = "Choose a Mood: happy, sad, tired, love, nervous, energetic, heartbroken, jealous, inspirational, pumpup, femaleempowerment, party, random "  
    return message
