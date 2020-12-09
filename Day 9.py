from itertools import combinations

l = 25
num = 25918798
with open("input9.txt", "r") as f:
    lst = [int(x) for x in f.read().splitlines()]

    for i in range(l, len(lst)):
        sums = list(map(sum, combinations(lst[i-l:], 2)))
        if lst[i] not in sums:
            print(lst[i])
            break

    print()

    for i in range(len(lst)):
        lst2 = []
        offset = 0
        while sum(lst2) <= num:
            if sum(lst2) == num and lst2[0] != num:
                print(min(lst2) + max(lst2))
                break
            elif i + offset > len(lst) - 1:
                break

            lst2.append(lst[i + offset])
            offset += 1