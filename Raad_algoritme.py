from Feedback import feedback
import random

antwoord = [1,1,2,1]
print('Antwoord: ',antwoord)


def alg():
    combi_lijst = gen()
    gok = random.choice(combi_lijst) # eerste gok
    print('Gok: ',gok)
    feedback(gok,antwoord)



def gen():
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