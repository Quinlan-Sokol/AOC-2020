from itertools import permutations, combinations_with_replacement, chain
from copy import deepcopy

offsets = set(chain.from_iterable([list(permutations(c, 4)) for c in list(combinations_with_replacement([-1, 1, 0], 4))]))
offsets.remove((0, 0, 0, 0))

def printGrid(g):
    for p in g:
        print("\n".join(["".join(x) for x in p]))
        print()

def getNeighbors(p, g):
    x = p[0]
    y = p[1]
    z = p[2]
    w = p[3]
    t = 0
    for offset in offsets:
        dx = offset[0]
        dy = offset[1]
        dz = offset[2]
        dw = offset[3]
        if g[w + dw][z + dz][y + dy][x + dx] == "#":
            t += 1
    return t

def bufferGrid2(g2):
    g = [[[["."] * (len(g2[0][0][0])) for y in range(len(g2[0][0]))] for x in range(len(g2[0]))]] + g2 + [[[["."] * (len(g2[0][0][0])) for y in range(len(g2[0][0]))] for x in range(len(g2[0]))]]
    for k in range(len(g)):
        g[k] = bufferGrid(g[k])
    return g

def bufferGrid(g2):
    g = [[["."] * (len(g2[0][0])) for x in range(len(g2[0]))]] + g2 + [[["."] * (len(g2[0][0])) for x in range(len(g2[0]))]]
    for i in range(len(g)):
        g[i] = [["."] * (len(g[i]))] + g[i] + [["."] * (len(g[i]))]
        for j in range(len(g[i])):
            g[i][j] = ["."] + g[i][j] + ["."]
    return g

with open("input17.txt", "r") as f:
    grid = [[[list(x) for x in f.read().splitlines()]]]
    grid = bufferGrid2(grid)

    for k in range(6):
        grid = bufferGrid2(grid)

        newGrid = deepcopy(grid)
        for w in range(1, len(grid) - 1):
            for z in range(1, len(grid[w]) - 1):
                for y in range(1, len(grid[w][z]) - 1):
                    for x in range(1, len(grid[w][z][y]) - 1):
                        n = getNeighbors([x, y, z, w], grid)
                        c = grid[w][z][y][x]
                        if c == "#" and 2 <= n <= 3:
                            newGrid[w][z][y][x] = "#"
                        elif c == "." and n == 3:
                            newGrid[w][z][y][x] = "#"
                        else:
                            newGrid[w][z][y][x] = "."

        grid = newGrid

    #printGrid(grid)
    #print(list(chain.from_iterable(chain.from_iterable(grid))).count("#"))
    print(list(chain.from_iterable(chain.from_iterable(chain.from_iterable(grid)))).count("#"))