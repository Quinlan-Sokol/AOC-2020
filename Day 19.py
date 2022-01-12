from itertools import product, chain


with open("input19.txt", "r") as f:
    dct = dict()
    lst = []
    messages = []
    b = True
    for line in f.read().splitlines():
        if line == "":
            b = False
        elif b:
            if "\"" in line:
                dct[line.split(": ")[0]] = [line.split(": ")[1][1]]
            else:
                lst.append(line)
        else:
            messages.append(line)

    while len(lst) > 0:
        for line in lst[:]:
            keys = set(line.split(": ")[1].replace(" | ", " ").split(" "))
            if all([k in dct for k in keys]):
                cache = []
                for part in line.split(": ")[1].split(" | "):
                    print(len([dct[x] for x in part.split(" ")][0]))
                    cache.append(["".join(x) for x in list(product(*[dct[x] for x in part.split(" ")]))])
                dct[line.split(": ")[0]] = list(chain.from_iterable(cache))
                lst.remove(line)

    print(len(set(messages).intersection(set(dct["0"]))))