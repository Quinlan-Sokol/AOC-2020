from functools import lru_cache
with open("input10.txt", "r") as f:
    lst = [int(x) for x in f.read().splitlines()]
    lst.append(max(lst) + 3)

    ones = 0
    threes = 0
    cur = 0

    while cur < max(lst):
        for n in range(cur+1, cur+4):
            if n in lst:
                if n - cur == 1: ones += 1
                elif n - cur == 3: threes += 1
                cur = n
                break

    print(ones*threes)

    @lru_cache(maxsize=1000000000)
    def findPaths(cur):
        if cur == max(lst):
            return 1
        else:
            t = 0
            for n in range(cur+1, cur+4):
                if n in lst:
                    t += findPaths(n)
            return t

    print(findPaths(0))