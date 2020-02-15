from Feedback import feedback
import random




def alg(antwoord,combi_lijst):
    print('Antwoord = ', antwoord)
    gok = random.choice(combi_lijst)  # eerste gok
    nieuwe_feedback = feedback(gok, antwoord)

    tijd = 0
    while len(combi_lijst) != 1:
        tijd += 1
        combi_lijst = vergelijken(combi_lijst, gok, nieuwe_feedback)
        gok = random.choice(combi_lijst)
        #print("Nieuwe gok:",gok)
        nieuwe_feedback = feedback(gok,antwoord)
    oplossing = combi_lijst[0]
    print('Aantal zetten', tijd, '---', 'Antwoord =', combi_lijst[0],'\n')
    return oplossing, tijd


def vergelijken(combi_lijst, gok, oude_feedback):
    nieuwe_lijst = [] #Tijdelijk
    for combinatie in combi_lijst:
        nieuwe_feedback = feedback(combinatie, gok)
        if nieuwe_feedback == oude_feedback:
            nieuwe_lijst.append(combinatie)
    combi_lijst = nieuwe_lijst

    return combi_lijst














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

def test():  #Test de gemiddelde snelheid
    pogingen = 100 # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0

    lst = gen()
    while keer != pogingen:
        ans, tijd = alg(random.choice(lst),lst)
        keer += 1
        totaal += tijd
    print('gem',totaal/keer)

#test()