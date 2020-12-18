from itertools import chain
from copy import deepcopy

def getSeats(p, grid):
    def findSeat(pos, delta):
        if pos[0] < 0 or pos[0] > len(grid)-1 or pos[1] < 0 or pos[1] > len(grid[0])-1:
            return 0

        c = grid[pos[0]][pos[1]]
        if c == "L": return 0
        elif c == "#": return 1
        else:
            return findSeat([pos[0] + delta[0], pos[1] + delta[1]], delta)

    return sum(map(lambda x : findSeat([p[0] + x[0], p[1] + x[1]], x), [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,-1], [-1,1]]))


with open("input11.txt", "r") as f:
    lst = [list(x) for x in f.read().splitlines()]
    lst2 = lst[::]

    while True:
        grid = deepcopy(lst)

        for i in range(len(lst)):
            for j in range(len(lst[i])):
                c = lst[i][j]
                t = 0
                if j+1 < len(lst[i]):
                    if lst[i][j+1] == "#":
                        t += 1
                    if i+1 < len(lst):
                        if lst[i+1][j+1] == "#":
                            t += 1
                    if i-1 >= 0:
                        if lst[i-1][j+1] == "#":
                            t += 1
                if j-1 >= 0:
                    if lst[i][j-1] == "#":
                        t += 1
                    if i+1 < len(lst):
                        if lst[i+1][j-1] == "#":
                            t += 1
                    if i-1 >= 0:
                        if lst[i-1][j-1] == "#":
                            t += 1
                if i+1 < len(lst):
                    if lst[i+1][j] == "#":
                        t += 1
                if i-1 >= 0:
                    if lst[i-1][j] == "#":
                        t += 1

                if c == "L" and t == 0:
                    grid[i][j] = "#"
                elif c == "#" and t >= 4:
                    grid[i][j] = "L"

        if grid == lst:
            break
        else:
            lst = grid

    print(list(chain.from_iterable(lst)).count("#"))

    while True:
        grid = deepcopy(lst2)

        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                c = lst2[i][j]

                n = getSeats([i, j], lst2)
                if c == "L" and n == 0:
                    grid[i][j] = "#"
                elif c == "#" and n >= 5:
                    grid[i][j] = "L"

        if grid == lst2:
            break
        else:
            lst2 = grid

    print(list(chain.from_iterable(lst2)).count("#"))
