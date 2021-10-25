import random
def exercise9():
    a = random.randint(1,9)
    b = int(input("Choose a number between 1 and 9!"))
    if b>9:
        print("Invalid Number")
    elif a == b:
    	print("You chose the correct number!")
    elif a > b:
	    print("Your number is too small!")
    elif a < b:
	    print("Your number is too big")
    else:
	    print("Your number is not valid!")

    print(f"The number was {a}!")
#exercise9()
def exercise9a():
    while True:
        a = random.randint(1, 9)
        b = int(input("Choose a number between 1 and 9!"))
        c = input("Do you want to exit?")
        if c == "exit":
            exit()
        elif a == b:
            print("You chose the correct number!")
        elif a > b:
            print("Your number is too big!")
        elif a < b:
            print("Your number is too small")
        else:
            print("Your number is not valid!")
#exercise9a()

def exercise9b():
    a = random.randint(1, 9)
    while True:
        b = int(input("Choose a number between 1 and 9!"))
        c = 0
        if a == "exit":
            exit()
        elif a == b:
            print("You chose the correct number!")
            exit()
        elif a > b:
            print("Your number is too small!")


            c = c + 1
        elif a < b:
            print("Your number is too big")
            c = c + 1
        else:
            print("Your number is not valid!")
        print(f"You took {c} guesses")
exercise9b()