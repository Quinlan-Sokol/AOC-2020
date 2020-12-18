from collections import defaultdict

with open("input14.txt", "r") as f:
    lst = f.read().splitlines()
    mask = ["X"]*36
    mem = defaultdict(int)

    for line in lst:
        if "mask" in line:
            mask = list(line.split(" = ")[1])
        else:
            address = line.split("]")[0][4:]
            val = int(line.split(" = ")[1])
            binary = [x for x in bin(val)[2:]]
            binary = ["0"]*(36 - len(binary)) + binary

            newBinary = list(map(lambda x,y : x if y == "X" else y, binary, mask))
            mem[address] = int("".join(newBinary), 2)

    print(sum(mem.values()))
    print()

    mask = ["X"] * 36
    mem = defaultdict(int)

    for line in lst:
        if "mask" in line:
            mask = list(line.split(" = ")[1])
        else:
            address = int(line.split("]")[0][4:])
            val = int(line.split(" = ")[1])
            binary = [x for x in bin(address)[2:]]
            binary = ["0"] * (36 - len(binary)) + binary

            newBinary = list(map(lambda x, y: x if y == "0" else "1" if y == "1" else "F", binary, mask))

            q = [[newBinary, 0]]
            while len(q) < 2**(newBinary.count("F")):
                e = q[0]
                q = q[1:]
                num = e[0]
                i = e[1]

                if num[i] == "F":
                    q.append([num[:i] + ["1"] + num[i+1:], i+1])
                    q.append([num[:i] + ["0"] + num[i + 1:], i + 1])
                else:
                    q.append([num, i + 1])

            for l in q:
                mem[int("".join(l[0]), 2)] = val

    print(sum(mem.values()))