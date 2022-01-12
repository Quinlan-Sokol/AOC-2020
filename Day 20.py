from copy import deepcopy, copy
from functools import reduce
from itertools import chain

import numpy as np

class Tile:

    def __init__(self, n, g):
        self.num = n
        self.grid = g

        self.top = g[0]
        self.bottom = g[-1]
        self.left = list(zip(*g))[0]
        self.right = list(zip(*g))[-1]

    def getMatches(self, l, t):
        lst = []
        g = deepcopy(self.grid)

        for k in range(2):
            for j in range(4):
                top = "".join(g[0])
                left = "".join(list(zip(*g))[0])

                valid = True
                if l is not None:
                    if "".join(l) != left:
                        valid = False
                if t is not None:
                    if "".join(t) != top:
                        valid = False
                if valid:
                    lst.append(Tile(self.num, g))

                g = np.rot90(g)
            g = np.flipud(g)
        return lst


def part2(g):
    b = True
    monster = [[0,1],[1,2],[4,2],[5,1],[6,1],[7,2],[10,2],[11,1],[12,1],[13,2],[16,2],[17,1],[18,1],[18,0],[19,1]]
    for k in range(2):
        if b:
            for j in range(4):
                c = 0
                for y in range(len(g)-3):
                    for x in range(len(g[y])-19):
                        if all([g[p[1] + y][p[0] + x] == "#" for p in monster]):
                            c += 1

                if c > 0:
                    print(list(chain.from_iterable(g)).count("#") - c * len(monster))
                    b = False
                    break
                g = np.rot90(g)
        g = np.flipud(g)

    #print("\n".join(["".join(row) for row in g]))


with open("input20.txt", "r") as f:
    lst = []
    temp = []
    for line in f.read().splitlines():
        if line == "":
            lst.append(Tile(int(temp[0].split(" ")[1][:-1]), [list(x) for x in temp[1:]]))
            temp = []
        else:
            temp.append(line)
    lst.append(Tile(int(temp[0].split(" ")[1][:-1]), [list(x) for x in temp[1:]]))

    size = int((len(lst))**.5)

    part2([list(line) for line in open("input20part2.txt", "r").read().splitlines()])

    def solve(tiles, grid):

        for tile in tiles:
            if len(grid[-1]) == size:
                grid.append([])

            leftTile = grid[-1][-1] if len(grid[-1]) > 0 else None
            topTile = grid[-2][len(grid[-1])] if len(grid) > 1 else None
            matches = tile.getMatches(leftTile if leftTile is None else leftTile.right,
                                      topTile if topTile is None else topTile.bottom)

            for m in matches:
                newList = copy(tiles)
                newList.remove(tile)
                newGrid = deepcopy(grid)
                newGrid[-1].append(m)
                return solve(newList, newGrid)

        return grid

    grid = None
    b = True
    for t in lst:
        if b:
            transformations = []
            g = deepcopy(t.grid)

            for k in range(2):
                for j in range(4):
                    transformations.append(Tile(t.num, g))
                    g = np.rot90(g)
                g = np.flip(g)

            for tile in transformations:
                l = lst[:]
                l.remove(t)
                r = solve(l, [[tile]])

                if len(r) == size:
                    if len(r[-1]) == size:
                        print(r[0][0].num * r[0][-1].num * r[-1][0].num * r[-1][-1].num)

                        def removeBorder(gr):
                            return [row[1:-1] for row in gr[1:-1]]

                        grid = [(list(map(lambda x : removeBorder(x.grid if type(x.grid) is list else x.grid.tolist()), row))) for row in r]
                        grid = [reduce(lambda x,res : np.concatenate((x, res), axis=1), row) for row in grid]
                        grid = reduce(lambda x,res : np.concatenate((x, res), axis=0), grid).tolist()

                        b = False
                        break

    #part2(grid)
    #print("\n".join(["".join(row) for row in grid]))
