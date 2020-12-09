import functools
with open("input6.txt", "r") as f:
    lst = f.read().splitlines()

    t = 0
    t2 = 0

    s = set()
    lst2 = []
    for i in range(len(lst)):
        str = lst[i]
        if str == "" or i == len(lst) - 1:
            if i == len(lst) - 1:
                s.update(set([x for x in str]))

            t += len(s)
            t2 += len(functools.reduce(lambda x,y : x.intersection(y), lst2, s))

            s = set()
            lst2 = []
        else:
            s.update(set([x for x in str]))
            lst2.append(set([x for x in str]))

    print(t)
    print(t2)