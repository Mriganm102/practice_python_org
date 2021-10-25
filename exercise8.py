def exercise8():
    while True:
        a = input("Player 1, choose 'rock', 'paper', or 'scissors'")
        print("No Looking\n"*100)
        b = input("Player 2, choose 'rock', 'paper', or 'scissors'")
        if a == "rock" and b == "rock":
            print("Draw")
        elif a == "rock" and b == "paper":
            print("Player 2 wins")
            return 2
        elif a == "rock" and b == "scissors":
            print("Player 1 wins")
            return 1
        elif a == "paper" and b == "rock":
            print("Player 1 wins")
            return 1
        elif a == "paper" and b == "paper":
            print("Draw")
        elif a == "paper" and b == "scissors":
            print("Player 2 wins")
            return 2
        elif a == "scissors" and b == "rock":
            print("Player 2 wins")
            return 2
        elif a == "scissors" and b == "paper":
            print("Player 1 wins")
            return 1
        elif a == "scissors" and b == "scissors":
            print("Draw")
        else:
            print("You didn't enter a valid answer")
            return "error"
exercise8()
