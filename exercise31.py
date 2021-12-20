class exercise31(object):
    print("Welcome to Hangman")
    word = 'hello'
    dict1 = {}
    dict2 = {}
    guesses = 0
    for i in range(len(word)):
        dict1[i] = word[i]
        dict2[i] = '*'
    while True:
        user_input = input("What is your letter")
        for i in range(len(word)):
            if user_input == word[i]:
                dict2[i] = word[i]
            else:
                print("Incorrect, try again")
            guesses = guesses + 1
        print(dict2)
        if dict1 == dict2:
            print("You Won!")
            exit()

def main():
    e31 = exercise31()
if __name__ == '__main__':
    main()