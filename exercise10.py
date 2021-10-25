import random
def exercise10():
    """
    Pre-condition = 2 lists
    Take 2 lists and write a program that returns a list that contains
    only the elements that are common between the lists without duplicates.
    Post-condition= returns the elements that are the same between the 2 list
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a = ([x for x in a for y in b if x == y])
    a1 = []
    for x in a:
        if x not in a1:
            a1.append(x)
    print(a1)
#exercise10()

def exercise10a():
    a = []
    b = []
    for x in range(10):
        z = random.randint(1,20)
        c = random.randint(1,20)
        a.append(z)
        b.append(c)
    a = ([x for x in a for y in b if x == y])
    a1 = []
    for x in a:
        if x not in a1:
            a1.append(x)
    print(a1)
exercise10a()