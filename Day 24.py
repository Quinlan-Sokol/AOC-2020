from copy import copy

dct = {"se" : "0",
       "sw" : "1",
       "ne" : "2",
       "nw" : "3",
       "e" : "4",
       "w" : "5"}
s = set()

for line in open("input24.txt", "r").read().splitlines():
    for k in dct:
        line = line.replace(k, dct[k])

    posX = 0
    posY = 0
    posZ = 0
    for n in line:
        if n == "0": #se
            posY -= 1
            posZ += 1
        elif n == "1": #sw
            posX -= 1
            posZ += 1
        elif n == "2": #ne
            posX += 1
            posZ -= 1
        elif n == "3": #nw
            posY += 1
            posZ -= 1
        elif n == "4": #e
            posY -= 1
            posX += 1
        elif n == "5": #w
            posY += 1
            posX -= 1

    if (posX, posY, posZ) in s:
        s.remove((posX, posY, posZ))
    else:
        s.add((posX, posY, posZ))

print(len(s))
print()


def getAdjacent(pos):
    return [tuple(map(lambda x,y : x+y, x, pos)) for x in [(0,1,-1), (-1,1,0), (-1,0,1), (0,-1,1), (1,-1,0), (1,0,-1)]]


for k in range(100):
    whites = set()

    newS = set()
    for tile in s:
        adjacent = getAdjacent(tile)

        numBlack = 0
        for t in adjacent:
            if t in s:
                numBlack += 1
            else:
                whites.add(t)

        if numBlack == 0 or numBlack > 2:
            pass
        else:
            newS.add(tile)

    for tile in whites:
        adjacent = getAdjacent(tile)
        numBlack = 0
        for t in adjacent:
            if t in s:
                numBlack += 1

        if numBlack == 2:
            newS.add(tile)

    s = copy(newS)

print(len(s))