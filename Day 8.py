
def run(lst):
    acc = 0
    i = 0
    visited = []

    while True:
        if i > len(lst) - 1 or i in visited: break
        line = lst[i]
        visited.append(i)

        if "acc" in line:
            acc += int(line.split(" ")[1])
            i += 1
        elif "jmp" in line:
            i += int(line.split(" ")[1])
        elif "nop" in line:
            i += 1

    return [i > len(lst) - 1, acc]

with open("input8.txt", "r") as f:
    lines = f.read().splitlines()

    acc = 0
    i = 0
    visited = []

    while True:
        if i > len(lines) or i in visited: break
        line = lines[i]
        visited.append(i)

        if "acc" in line:
            acc += int(line.split(" ")[1])
            i += 1
        elif "jmp" in line:
            i += int(line.split(" ")[1])
        elif "nop" in line:
            i += 1
    print(acc)


    for i in range(len(lines)):
        if "jmp" in lines[i]:
            lst2 = lines[::]
            lst2[i] = "nop " + lines[i].split(" ")[1]
            r = run(lst2)
            if r[0]:
                print(r[1])
        elif "nop" in lines[i]:
            lst2 = lines[::]
            lst2[i] = "jmp " + lines[i].split(" ")[1]
            r = run(lst2)
            if r[0]:
                print(r[1])
