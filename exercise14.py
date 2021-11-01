def exercise14():
    """Pre-Condition - A list of numbers(Can be duplicates)
        Use lists to make a list without duplicates from the first list
        Post-condition - A list of numbers from the first list with no duplicates"""
    a = [1, 3, 5, 6, 7, 6, 8, 9, 9, 9]
    y = []
    for x in a:
        if x not in y:
            y.append(x)
    return y
print(exercise14())
def exercise14a():
    """Pre-Condition - A list of numbers(Can be duplicates)
    Use sets to make a list without duplicates from the first list
    Post-condition - A list of numbers from the first list with no duplicates"""
    a = [1, 3, 5, 6, 7, 6, 8, 9, 9, 9]
    set1 = set(a)
    list1 = list(set1)
    return list1
print(exercise14a())