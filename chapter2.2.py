def union(set1, set2):
    set1 = list(set1)
    set2 = list(set2)
    unions = []
    for i in set1:
        unions.append(i)
    for i in set2:
        if i not in unions:
            unions.append(i)
    print(unions)

union({1,2,3,4}, {3,4,5,6})

def intersection(set1, set2):
    set1 = list(set1)
    set2 = list(set2)
    intersections = [x for x in set1 for y in set2 if x == y]
    print(intersections)
intersection({1,2,3,3,4}, {3,3,4,5,6})

def complement(set1, universal_set):
    set1 = list(set1)
    list1 = []
    for i in universal_set:
        if i not in set1:
            list1.append(i)
    print(list1)

complement({1,2,3,4}, range(20))
