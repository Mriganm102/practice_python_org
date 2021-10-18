import random
def exercise5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    z = []
    for x in a:
        for y in b:
            if x == y:
                z.append(x)
    print(z)
exercise5()

def exercise5a(x, y, a, b, c, d):
    z1 = []
    z2 = []
    z = []
    for number in range(int(x)):
        z1.append(random.randint(a, b))
    for num in range(int(y)):
        z2.append(random.randint(c, d))
    for s in z1:
        for t in z2:
            if s == t:
                z.append(s)
    print(z)
exercise5a(4, 5, 1, 11, 5, 9)

def exercise5b(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]):
     print([x for x in a for y in b if x == y])
exercise5b()
