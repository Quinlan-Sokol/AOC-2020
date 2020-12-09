t = 1
with open("input3.txt", "r") as f:
    lst = [list(x) for x in f.read().splitlines()]
    for p in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        x, y, c = 0, 0, 0
        while y < len(lst):
            if lst[y][x] == "#":
                c += 1
            x = (x + p[0]) % len(lst[0])
            y += p[1]
        t *= c
    print(t)