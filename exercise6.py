def exercise6(word):
    b = []
    for a in word:
        b.append(a)
    reversedName = b[::-1]
    if reversedName == b:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
exercise6("bobjj")