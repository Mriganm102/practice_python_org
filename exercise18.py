import random
def exercise18():
    print("Welcome to the Cow and Bull Game")
    random_number = random.randint(1000,9999)
    while True:
        user_input = input("What is your 4-digit number?")
        cows = 0
        bulls = 0
        list1 = []
        list2 = []
        digit = [1,1,1,1]
        for x in str(random_number):
            list1.append(x)
        for x in user_input:
            list2.append(x)
        if list1[0] == list2[0]:
            digit[0] = True
            cows = cows+1
        else:
            digit[0] = False
        if list1[1] == list2[1]:
            digit[1] = True
            cows = cows + 1
        else:
            digit[1] = False
        if list1[2] == list2[2]:
            digit[2] = True
            cows = cows + 1
        else:
            digit[2] = False
        if list1[3] == list2[3]:
            digit[3] = True
            cows = cows + 1
        else:
            digit[3] = False

        for x in range(0,4):
            if list2[x] in list1 and digit[x] == False:
                bulls = bulls + 1
        if list1 == list2:
            print("The number was", random_number)
            return 'You won!'
        print("Cows : ", cows)
        print("Bulls : ", bulls)


#print(exercise18())


def exercise18b():
    print("Welcome to the Cow and Bull Game")
    #random_number = random.randint(1000,9999)
    random_number = 3478
    list1 = []
    for x in str(random_number):
        list1.append(x)
    list2 = [0,0,0,0]
    list3 = [0,0,0,0]
    digit = [1, 1, 1, 1]
    while True:
        user_input = input("What is your 4-digit number?")
        cows = 0
        bulls = 0
        for i,x in enumerate(user_input):
            list3[i] = list2[i]
            list2[i] = x

        if list1[0] == list2[0]:
            digit[0] = True
            cows = cows+1
        else:
            digit[0] = False
        if list1[1] == list2[1]:
            digit[1] = True
            cows = cows + 1
        else:
            digit[1] = False
        if list1[2] == list2[2]:
            digit[2] = True
            cows = cows + 1
        else:
            digit[2] = False
        if list1[3] == list2[3]:
            digit[3] = True
            cows = cows + 1
        else:
            digit[3] = False

        for x in range(0,4):
            if list3[x] != list2[x] and list3[x] == list1[x]:
                bulls = bulls + 1
        if list1 == list2:
            print("The number was", random_number)
            return 'You won!'
        print("Cows : ", cows)
        print("Bulls : ", bulls)

print(exercise18b())

