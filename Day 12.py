
with open("input12.txt", "r") as f:
    lst = f.read().splitlines()

    d = 0 #east
    p = [0, 0]
    for x in lst:
        c = x[0]
        n = int(x[1:])

        if c == "N":
            p[1] += n
        elif c == "S":
            p[1] -= n
        elif c == "E":
            p[0] -= n
        elif c == "W":
            p[0] += n
        elif c == "L":
            d -= n / 90
            if d < 0: d += 4
        elif c == "R":
            d += n / 90
            if d > 3: d -= 4
        elif c == "F":
            if d == 0:
                p[0] -= n
            elif d == 1:
                p[1] -= n
            elif d == 2:
                p[0] += n
            elif d == 3:
                p[1] += n


    print(abs(p[0]) + abs(p[1]))

    p = [0, 0]
    w = [-10, 1]
    for x in lst:
        c = x[0]
        n = int(x[1:])

        if c == "N":
            w[1] += n
        elif c == "S":
            w[1] -= n
        elif c == "E":
            w[0] -= n
        elif c == "W":
            w[0] += n
        elif c == "L":
            for i in range(int(n/90)):
                w = [w[1], -w[0]]
        elif c == "R":
            for i in range(int(n/90)):
                w = [-w[1], w[0]]
        elif c == "F":
            p = [p[0] + w[0]*n, p[1] + w[1]*n]

    print(abs(p[0]) + abs(p[1]))