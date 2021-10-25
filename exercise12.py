def exercise12():
    """
    Pre-condition is a = list of numbers
    Write a program that takes a list of numbers and
    makes a new list of only the first and last elements of the given list.
    Post-condition = the function returns the first and last elements of a
    """
    a = [0, 5, 10, 15, 20, 25, 35]
    b = len(a)
    c = a[0]
    bb = int(b) - 1
    d = []
    d.append(c)
    e = a[bb]
    d.append(e)
    print(d)
exercise12()
