def problem23():
#Trying to find if the function is onto
    domain = [1,2,3,5,7,9]
    range = [1,2,3,6,7,8,9]
    for i in domain:
        if i in range:
            pass
        else:
            return False
    return True
print(problem23())


def problem31():
#Trying to see if a number repeats in a sequence
    S = [1,2,3,4,5,6,7,8,9]
    A = []
    for i in S:
        for j in A:
            if i == j:
                return True
            A.append(i)
    return False

print(problem31())


def problem43(x):
#Trying to find where a number is located in a list
    sequence = [1,2,4,5,6,8,9]
    counter = -1
    for i in sequence:
        counter = counter + 1
        if x >= i:
            pass
        else:
            return counter
    return counter

print(problem43(7))

def problem57():
#Trying to find compatible times
    dictionary = {9.30:10, 9.50:10.15, 10:10.30, 10.10:10.25, 10.30:10.55, 10.15:10.45, 10.3:11, 10.45:11.30, 10.55:11.25, 11:11.15}
    compatible = [9,9.45]
    list1 = [9, 9.45]
    for i in dictionary:
        counter = -1
        for j in list1:
            counter = counter + 1
            if i >= j:
                pass
            else:
                list1.insert(counter, i)
        if i == list1[1]:
            pass
        else:
            compatible.append(i)
            compatible.append(dictionary[i])
            list1 = [i, dictionary[i]]
    print(compatible)
problem57()
