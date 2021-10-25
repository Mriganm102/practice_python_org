def division(x):
    y = range(1, int(x+1))
    list_of_numbers = []
    for a in y:
        if x % a == 0:
            list_of_numbers.append(a)
    print(list_of_numbers)
division(10)