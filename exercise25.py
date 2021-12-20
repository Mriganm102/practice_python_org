import random
class exercise_25(object):
    def exercise25(self):
        user_input = self.user_input
        computer_guess = random.randint(1, 100)
        guesses = 1
        min = 0
        print(computer_guess)
        max = 100
        while True:
            if computer_guess == int(user_input):
                print("The computer chose the correct number!")
                print(f"You took {guesses} guesses")
                exit()
            higher_lower_indicator = input("Is the number higher or lower?")
            if higher_lower_indicator == "lower":
                min = computer_guess
                computer_guess = random.randint(min,max)
                print(computer_guess)
            elif higher_lower_indicator == "higher":
                max = computer_guess
                computer_guess = random.randint(min, max)
                print(computer_guess)
            else:
                print("Invalid")
            guesses = guesses + 1
    def __init__(self):
        user_input = input("Choose a number between 1 and 100")
        self.user_input = user_input
        self.exercise25()

def main():
    exercise25 = exercise_25()

if __name__ == '__main__':
    main()