import math
with open("input5.txt", "r") as f:
    lst = f.read().splitlines()

    lst2 = []

    for str in lst:
        lower = 0
        upper = 127
        for s in str[:7]:
            if s == "F":
                upper = math.floor((upper + lower) / 2)
            else:
                lower = math.ceil((upper + lower) / 2)

        row = lower

        lower = 0
        upper = 7
        for s in str[7:]:
            if s == "L":
                upper = math.floor((upper + lower) / 2)
            else:
                lower = math.ceil((upper + lower) / 2)

        col = lower

        lst2.append((row * 8) + col)
    print(max(lst2))

    lst2 = sorted(lst2)
    for i in range(1, len(lst2) - 1):
        if lst2[i] - lst2[i-1] != 1:
            print(lst2[i] - 1)
            break