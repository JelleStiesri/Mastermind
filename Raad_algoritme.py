from Feedback import feedback
import random

antwoord = [3,6,2,3]
print('Antwoord: ',antwoord)


def alg():
    geraden = False
    combi_lijst = gen()
    eerste_gok = random.choice(combi_lijst)  # eerste gok

    print('Gok: ',eerste_gok)

    eerste_feedback = feedback(eerste_gok,antwoord)

    print('eerste feedback: ',eerste_feedback)
    print("lengte van lijst (0): ", len(combi_lijst))

    vergelijken(combi_lijst, eerste_gok, eerste_feedback)


def vergelijken(combi_lijst, gok, eerste_feedback):
     print()














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