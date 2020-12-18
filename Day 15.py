
lst = [int(x) for x in "7,14,0,17,11,1,2".split(",")]
dic = dict()
for x in range(len(lst)-1):
    dic[lst[x]] = x


def rindex(l, v):
    for i in range(len(l) - 1, -1, -1):
        if l[i] == v:
            return i

for i in range(len(lst), 30000000 + len(lst)):
    last = lst[-1]
    if last not in dic:
        lst.append(0)
    else:
        lst.append(len(lst) - dic[last] - 1)

    dic[last] = i-1


print(lst[30000000-1])
