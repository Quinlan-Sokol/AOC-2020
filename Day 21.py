from collections import defaultdict, Counter

lst = open("input21.txt", "r").read().splitlines()
dct = dict()
allIngredients = []

for line in lst:
    for allergen in line.split(" (contains ")[1][:-1].split(", "):
        if allergen not in dct:
            dct[allergen] = set(line.split(" (contains ")[0].split(" "))
        else:
            dct[allergen].intersection_update(line.split(" (contains ")[0].split(" "))
    allIngredients += line.split(" (contains ")[0].split(" ")

s = set()
for v in dct.values():
    s.update(v)

for v in s:
    while v in allIngredients:
        allIngredients.remove(v)
print(len(allIngredients))

allergens = dict()
while len(allergens) != len(dct):
    for k in dct:
        if len(dct[k]) == 1:
            v = list(dct[k])[0]
            allergens[k] = v

            for key in dct:
                if v in dct[key]:
                    dct[key].remove(v)
print(",".join(map(lambda x : allergens[x], sorted(allergens.keys()))))