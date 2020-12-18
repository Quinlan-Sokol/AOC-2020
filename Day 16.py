from functools import reduce
def valid(n, ranges):
    return any([r[0] <= n <= r[1] for r in ranges])

def validTicket(t, ranges):
    return all([valid(n, ranges) for n in t])

with open("input16.txt", "r") as f:
    lst = [x for x in f.read().splitlines() if x != ""]
    ranges = []
    tickets = []
    dic = dict()
    myTicket = []

    temp = 0
    for line in lst:
        if "ticket" in line:
            temp += 1
        else:
            if temp == 0:
                ranges.append([int(line.split(": ")[1].split(" or ")[0].split("-")[0]),
                               int(line.split(": ")[1].split(" or ")[0].split("-")[1])])
                ranges.append([int(line.split(": ")[1].split(" or ")[1].split("-")[0]),
                               int(line.split(": ")[1].split(" or ")[1].split("-")[1])])

                dic[line.split(": ")[0]] = [ranges[-2], ranges[-1]]
            elif temp == 1:
                tickets.append(list(map(int, line.split(","))))
                myTicket = tickets[-1]
            elif temp == 2:
                tickets.append(list(map(int, line.split(","))))

    s = 0
    for t in tickets:
        s += sum(filter(lambda x : not valid(x, ranges), t))
    print(s)

    tickets = [x for x in tickets if validTicket(x, ranges)]
    order = []

    for field in list(zip(*tickets)):
        validFields = []
        for k in dic:
            if validTicket(field, dic[k]):
                validFields.append(k)
        order.append(validFields)

    newOrder = [""]*len(order)
    while sum([len(x) for x in order]) > len(dic):
        for i in range(len(order)):
            if len(order[i]) == 1:
                f = order[i][0]
                newOrder[i] = f

                for k in range(len(order)):
                    if f in order[k]:
                        order[k].remove(f)

                break

    print(reduce(lambda x, y : x*y, [myTicket[newOrder.index(x)] for x in newOrder if "departure" in x]))