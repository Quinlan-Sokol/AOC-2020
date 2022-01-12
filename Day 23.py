input = "389125467"
lst = [int(x) for x in input]
index = 0
m = max(lst)

lst2 = lst + list(range(m+1, 1000001))

def getClosest(n, s, b):
    i = n-1
    while i != n:
        if i < 1:
            i = m if b else 1000000
        if i not in s:
            return i
        else:
            i -= 1

    cur = lst[0]
    sub = lst[1:4]
    lst = lst[:1] + lst[4:]

    des = lst.index(getClosest(cur, sub, True))
    lst = lst[:des+1] + sub + lst[des+1:]

    lst = lst[1:] + [lst[0]]

i = lst.index(1)
print(int("".join(map(str, lst[i+1:] + lst[:i]))))

for k in range(10000000):
    if k % 10 == 0:
        print(k)

    cur = lst2[0]
    sub = lst2[1:4]
    lst2 = lst2[:1] + lst2[4:]

    des = lst2.index(getClosest(cur, sub, False))
    lst2 = lst2[:des+1] + sub + lst2[des+1:]

    lst2 = lst2[1:] + [lst2[0]]
