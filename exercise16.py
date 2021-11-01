import random
def exercise16():
    list_of_letters = ["q", "r", "w", "e", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    Upper_list_of_letters = []
    for x in list_of_letters:
        y = x.upper()
        Upper_list_of_letters.append(y)
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ";", ":", '"', "'", "<", ">", ",", ".", "?", "/"]
    numbers = range(1,100)
    password = []
    for x in range(5):
        a = random.choice(list_of_letters)
        b = random.choice(Upper_list_of_letters)
        c = random.choice(symbols)
        d = random.choice(numbers)
        password.append(a)
        password.append(b)
        password.append(c)
        password.append(d)
    a = str(password)
    string1 = "".join(a)
    print("Your password is: ", string1)

exercise16()

def exercise16a():
    l = input("Weak or Strong Password")
    list_of_letters = ["q", "r", "w", "e", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    Upper_list_of_letters = []
    for x in list_of_letters:
        y = x.upper()
        Upper_list_of_letters.append(y)
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ";", ":", '"', "'", "<", ">", ",", ".", "?", "/"]
    numbers = range(1,100)
    password = []
    if l == "weak":
        for x in range(2):
            a = random.choice(list_of_letters)
            b = random.choice(Upper_list_of_letters)
            c = random.choice(symbols)
            d = random.choice(numbers)
            password.append(a)
            password.append(b)
            password.append(c)
            password.append(d)
    if l == "strong":
        for x in range(5):
            a = random.choice(list_of_letters)
            b = random.choice(Upper_list_of_letters)
            c = random.choice(symbols)
            d = random.choice(numbers)
            password.append(a)
            password.append(b)
            password.append(c)
            password.append(d)
    a = str(password)
    string1 = "".join(a)
    print("Your password is: ", string1)
exercise16a()