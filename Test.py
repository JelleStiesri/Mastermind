from itertools import permutations
def gen():
    perm = permutations([1, 2, 3, 4, 5, 6])
    mogelijkheden = []
    for i in list(perm):
        mogelijkheden.append(i)

    print(mogelijkheden)

gen()




