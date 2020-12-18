
timestamp = 1006697
lst = [x if x == "x" else int(x) for x in "13,x,x,41,x,x,x,x,x,x,x,x,x,641,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,661,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23".split(",")]
times = [int(x) for x in lst if not x == "x"]

c = timestamp
b = True
while b:
    for n in times:
        if c % n == 0:
            print((c-timestamp)*n)
            b = False
    c += 1

n = 0
for x in lst:
    if x != "x":
        print(n, x)
    n -= 1