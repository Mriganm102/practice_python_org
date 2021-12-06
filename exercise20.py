import random
def exercise20():
    list1 = list(range(5,16))
    a = random.randint(1,30)
    value = a in list1
    if value:
        print(a)
        return True
    else:
        print(a)
        return False
print(exercise20())