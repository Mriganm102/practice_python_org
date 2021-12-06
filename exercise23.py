with open('hi', 'r') as open_file:
    all_text = open_file.read()
list1 = all_text.split()
set1 = set(list1)
dicti = {}
list2 = list(set1)
for x in set1:
    dicti[x] = 0
for x in set1:
    for y in list1:
        if x == y:
            dicti[x] = dicti[x] + 1
print(dicti)
for x in list1:
    print(x)

