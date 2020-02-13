import random
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
            print('klaar')
            break
    lijst.sort(key=lambda x: x[0,1,2,3])

    print(lijst, len(lijst))

gen()




