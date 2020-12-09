
with open("input1.txt", "r") as f:
    lst = [int(x) for x in f.read().splitlines()]

    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == 2020:
                    print(lst[i] * lst[j] * lst[k])