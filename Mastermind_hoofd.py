import random



def mastermind():
    antwoord = []
    print("welke spelmodus wil je spelen",'\n',"1: Speler raadt, computer geeft code",'\n',"2: Computer raadt, speler geeft code")
    keuze = int(input('Keuze: '))
    if keuze == 1:
        for getal in range(4):
            los_getal = random.randrange(1, 7)
            antwoord.append(los_getal)
    elif keuze == 2:
        while True: #True todat user goede code geeft
            getallen = input("Geef een 4 cijferige code: ")
            if len(getallen) != 4:
                print('Probeer opnieuw')
            else:
                for getal in getallen:
                    getal = int(getal)
                    antwoord.append(getal)
                break








    print(antwoord)

mastermind()


