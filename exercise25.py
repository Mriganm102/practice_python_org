import random
def exercise25():
    a = random.randint(1, 100)
    c = 1
    b = input("Choose a number between 1 and 100")
    print(a)
    e = 0
    f = 100
    while True:
        if a == b:
            print("The computer chose the correct number!")
            print(f"You took {c} guesses")
            exit()
        if e == b:
            print("The computer chose the correct number!")
            print(f"You took {c} guesses")
            exit()
        if f == b:
            print("The computer chose the correct number!")
            print(f"You took {c} guesses")
            exit()
        d = input("Is the number higher or lower?")
        if d == "lower":
            e = random.randint(f, int(b))
            e = -1*e
            print(e)
        elif d == "higher":
            f = random.randint(int(b),-1*e)
            f= -1*f
            print(f)
        else:
            print("Invalid")
        c = c + 1
exercise25()