from Feedback import feedback
import random

antwoord = [1,1,2,1]
print('Antwoord: ',antwoord)


def alg():
    combi_lijst = gen()
    eerste_gok = random.choice(combi_lijst)  # eerste gok
    print('Gok: ',eerste_gok)
    eerste_feedback = feedback(eerste_gok,antwoord)
    print('eerste feedback: ',eerste_feedback)

    print("lengte van lijst: ", len(combi_lijst))
    tijd = 0
    nieuwe_lijst = []
    for combinatie in combi_lijst:

        tweede_feedback = feedback(combinatie,eerste_gok)
        if tweede_feedback == eerste_feedback:
            tijd += 1
            print(tijd,tweede_feedback)
            nieuwe_lijst.append(combinatie)
        else:
            combi_lijst.remove(combinatie)





    print("lengte van lijst 2e: ", len(nieuwe_lijst))
    print(tijd)
    tweede_gok = random.choice(combi_lijst)
    print('Gok: ',tweede_gok)










def gen(): # Maakt een lijst met alle mogelijke combinaties van de cijfers 1/6 en met 4 tekens te gelijk
    lijst = []
    fout = 0
    while True:
        combinatie = []
        for getal in range(4):
            los_getal = random.randrange(1, 7)
            combinatie.append(los_getal)
        if combinatie in lijst:
            fout = fout + 1
            continue
        else:
            lijst.append(combinatie)
        if len(lijst) == 1296: #aantal mogelijke combinaties
            break
    lijst.sort(key=lambda x: x[0])
    """SORTEREN AFMAKEN"""
    return(lijst)








alg()