def exercise6(word, word2):
    b = []
    c = []
    for a in word:
        b.append(a)
    for a in word2:
        c.append(a)
    reversedName = c[::-1]
    if reversedName == b:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
exercise6("hello", "olleh")