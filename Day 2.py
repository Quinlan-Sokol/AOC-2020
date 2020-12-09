
with open("input2.txt", "r") as f:
    lst = f.read().splitlines()
    t = 0
    for p in lst:
        min_n = int(p.split(": ")[0].split(" ")[0].split("-")[0])
        max_n = int(p.split(": ")[0].split(" ")[0].split("-")[1])
        l = p.split(": ")[0].split(" ")[1]
        str = p.split(": ")[1]

        if (str[min_n-1] == l or str[max_n-1] == l) and (str[min_n-1] != l or str[max_n-1] != l):
            t += 1

    print(t)