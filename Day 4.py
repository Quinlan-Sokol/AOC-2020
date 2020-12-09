import functools
with open("input4.txt", "r") as f:
    lst = f.read().splitlines()

    t = 0
    str = ""
    for s in lst:
        if s == "" or s == lst[-1]:
            if s == lst[-1]:
                str = str + s + " "

            dic = dict()
            for x in str.split(" ")[:-1]:
                dic[x.split(":")[0]] = x.split(":")[1]

            if "byr" in dic and "iyr" in dic and "eyr" in dic and "hgt" in dic and "hcl" in dic and "ecl" in dic and "pid" in dic:
                if 1920 <= int(dic["byr"]) <= 2002:
                    if 2010 <= int(dic["iyr"]) <= 2020:
                        if 2020 <= int(dic["eyr"]) <= 2030:
                            height = dic["hgt"]
                            n = int("".join([x for x in height if not x.isalpha()]))
                            end = "".join([x for x in height if x.isalpha()])
                            result = False
                            if end == "cm":
                                result = 150 <= n <= 193
                            elif end == "in":
                                result = 59 <= n <= 76

                            if result:
                                hair = dic["hcl"]
                                if hair[0] == "#" and len(hair) == 7 and functools.reduce(lambda x,y : x and y, [(x.isdigit() or 97 <= ord(x) <= 102) for x in hair[1:]]):
                                    eye = dic["ecl"]
                                    if eye in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                        if len(dic["pid"]) == 9 and functools.reduce(lambda x,y : x and y, [(x.isdigit() for x in dic["pid"])]):
                                            t += 1

            str = ""
        else:
            str = str + s + " "

    print(t)