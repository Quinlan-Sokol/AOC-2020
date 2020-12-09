


def part1(bag, d):
    if bag == "shiny gold":
        return True
    else:
        return any(map(lambda x : part1(x[1], d), d[bag]))

def part2(bag, d):
    #print(bag)
    if len(d[bag]) == 0:
        return 1
    else:
        return sum(map(lambda x : x[0] * part2(x[1], d), d[bag])) + 1


with open("input7.txt", "r") as f:
    lst = f.read().splitlines()

    dic = dict()
    for line in lst:
        if "no other bags" in line:
            dic[line.split(" ")[0] + " " + line.split(" ")[1]] = []
        else:
            bags = line.split(" contain ")[1].split(", ")
            dic[line.split(" ")[0] + " " + line.split(" ")[1]] = [[int(x.split(" ")[0]), x.split(" ")[1] + " " + x.split(" ")[2]] for x in bags]

    t = 0
    for k in dic:
        if part1(k, dic) and k != "shiny gold":
            t += 1

    print(t)
    print(part2("shiny gold", dic) - 1)