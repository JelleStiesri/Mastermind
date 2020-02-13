def feedback(gok, antwoord):
    wit = 0
    zwart = 0
    for item in gok: #voor de witte feedback
        if item in antwoord:
            wit += 1
    index = 0
    for item in gok: #voor de zwarte feedback
        if item == antwoord[index]:
            zwart += 1
        index += 1
    wit = wit-zwart
    print('Zwart:',zwart, ' -- ','Wit:',wit)
    return(zwart, wit)



def gok():
    gok = []
    while True:  # True todat user goede code geeft
        getallen = input("Gok: ")

        if len(getallen) != 4:
            print('Probeer opnieuw')
        else:
            for getal in getallen:
                getal = int(getal)
                gok.append(getal)
            break
    feedback(gok, [3, 7, 2, 3])
    """OPLOSSEN: feedback is 2,1 als je 3433 invult"""

#print(feedback([1, 7, 3, 2], [3, 7, 2, 3]))


while True:
    gok()