import random
class cowsandbulls(object):
    print("Welcome to the Cow and Bull Game")
    #random_number = random.randint(1000,9999)
    random_number = 3478
    user_input = input("What is your 4-digit number?")
    cows = ("You have ", 0 ," cows!")
    bulls = ("You have ", 0, " bulls!")
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    if random_number == int(user_input):
        print("You got it right")
        print(cows, bulls)
    print(random_number)
    for x in str(random_number):
        list1.append(x)
    for x in user_input:
        list2.append(x)
    for i,x in enumerate(list1):
        for j,y in enumerate(list2):
            if (i) == (j):
                if x == y:
                    list3.append(x)
                    list4.append(i)
                    #cows = len(list3)
    digit1 = False
    digit2 = False
    digit3 = False
    digit4 = False
    for x in range(4):
        if list1[x] == list2[x]:
            cows = cows + 1
    print(cows)
def main():
    exercise18 = cowsandbulls()
if __name__ == '__main__':
    main()


