# Euclid game script from MAP
import random

series = int(input("Type number of series: "))

for x in range(0, series):

    print("Series -", x+1)
    a = random.randint(1, 1000000000)
    b = random.randint(1, 1000000000)
    print("a =", a, "b =", b)
    i = 0
    c = a
    d = b

    # My algorithm
    while a != b:
        i += 1
        if a > b:
            a = a - b
        else:
            b = b - a
    print("My algorithm")
    print("Number of iterations:", i)
    print("Final a + b =", a+b, "\n")

    # MYR algorithm
    i = 0
    while True:
        if c == d or c == 0 or d == 0:
            break
        else:
            if c > d:
                c = c - d
            else:
                d = d - c
        i += 1
    print("MYR algorithm")
    print("Number of iterations:", i)
    print("Final a + b =", c + d, "\n")
