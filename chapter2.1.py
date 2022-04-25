def power_set(set1):
    set1 = list(set1)
    cardinality = len(set1)
    binary = []
    for i in range(2**cardinality):
        b = bin(i)[2:]
        l = len(b)
        b = str(0) * (cardinality - l) + b
        binary.append(b)
    list1 = []
    list2 = []
    powerset = []
    for x in binary:
        for y in x:
            list1.append(y)
    binary1 = [list1[x:x + cardinality] for x in range(0, len(list1), cardinality)]
    for x in binary1:
        for y in range(0, cardinality):
            if x[y] == "1":
                list2.append(set1[y])
        powerset.append(list2)
        list2 = []
    print(powerset)
    return powerset




power_set({})
power_set({"a"})
power_set({1,2,3})
power_set({'a', 'b', 'c', 'd'})
power_set({1,2,3,4,5})
power_set({'a', 'b', 'c', 'd','e', 'f'})
power_set({1,2,3,4,5,6,7})