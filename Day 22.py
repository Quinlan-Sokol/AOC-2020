
lst1 = []
lst2 = []
b = True
for line in open("input22.txt", "r").read().splitlines():
    if "Player" in line:
        pass
    elif line == "":
        b = False
    elif b:
        lst1.append(int(line))
    else:
        lst2.append(int(line))


def recurse(l1, l2, cache):
    while (len(l1) > 0 and len(l2) > 0) and "".join(map(str, l1)) + ":" + "".join(map(str, l2)) not in cache:
        cache.add("".join(map(str, l1)) + ":" + "".join(map(str, l2)))
        c1 = l1.pop(0)
        c2 = l2.pop(0)
        if len(l1) >= c1 and len(l2) >= c2:
            r = recurse(l1[:c1], l2[:c2], set())
            if r[0] == 1:
                l1 += [c1, c2]
            else:
                l2 += [c2, c1]
        elif c1 > c2:
            l1 += [c1, c2]
        else:
            l2 += [c2, c1]

    if (len(l1) > 0 and len(l2) > 0) or len(l2) == 0:
        return [1, l1]
    else:
        return [2, l2]


r = recurse(lst1[:], lst2[:], set())[1]

while len(lst1) > 0 and len(lst2) > 0:
    c1 = lst1.pop(0)
    c2 = lst2.pop(0)
    if c1 > c2:
        lst1 += [c1, c2]
    else:
        lst2 += [c2, c1]

print(sum(map(lambda x,y : x*y, lst1 + lst2, list(range(len(lst1 + lst2), 0, -1)))))
print(sum(map(lambda x,y : x*y, r, list(range(len(r), 0, -1)))))
