
def solve1(eq):
    while "(" in eq:
        start = eq.index("(")
        d = 1
        for i in range(start + 1, len(eq)):
            if eq[i] == "(":
                d += 1
            elif eq[i] == ")":
                d -= 1
                if d == 0:
                    eq = eq[:start] + solve1(eq[start+1:i]) + eq[i+1:]
                    break

    while len(eq) > 1:
        eq = [str(eval(" ".join(eq[:3])))] + eq[3:]

    return eq


def solve2(eq):
    while "(" in eq:
        start = eq.index("(")
        d = 1
        for i in range(start + 1, len(eq)):
            if eq[i] == "(":
                d += 1
            elif eq[i] == ")":
                d -= 1
                if d == 0:
                    eq = eq[:start] + solve2(eq[start+1:i]) + eq[i+1:]
                    break

    while "+" in eq:
        i = eq.index("+")
        eq = eq[:i-1] + [str(eval(" ".join(eq[i-1:i+2])))] + eq[i+2:]

    return [str(eval(" ".join(eq)))]


with open("input18.txt", "r") as f:
    lst = [list(x.replace(" ", "")) for x in f.read().splitlines()]

    s1 = 0
    for line in lst:
        s1 += int(solve1(line)[0])
    print(s1)

    s2 = 0
    for line in lst:
        s2 += int(solve2(line)[0])
    print(s2)
