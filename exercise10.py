import random
def exercise10():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a = ([x for x in a for y in b if x == y])
    a1 = []
    for x in a:
        if x not in a1:
            a1.append(x)
    print(a1)
exercise10()

def exercise10a():
    a = []
    b = []
    for x in range(10):
        z = random.randint(1,20)
        c = random.randint(1,20)
        a.append(z)
        b.append(c)
    print(a)
    print(b)
    a = ([x for x in a for y in b if x == y])
    a1 = []
    for x in a:
        if x not in a1:
            a1.append(x)
    print(a1)
exercise10a()