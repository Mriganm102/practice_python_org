class exercise_26():
    def exercise26(self):
        game = [0,
                1,2,2,
                1,2,1,
                1,2,1]
        if game[1] == game[2]:
            if game[2] == game[3]:
                return (f"Player{game[1]} has won")
        if game[1] == game[4]:
            if game[4] == game[7]:
                return (f"Player{game[1]} has won")
        if game[1] == game[5]:
            if game[5] == game[9]:
                return (f"Player{game[1]} has won")
        if game[4] == game[5]:
            if game[5] == game[6]:
                print(f"Player{game[4]} has won")
        if game[2] == game[5]:
            if game[5] == game[8]:
                print(f"Player{game[2]} has won")
        if game[3] == game[6]:
            if game[6] == game[9]:
                print(f"Player{game[3]} has won")
        if game[7] == game[8]:
            if game[8] == game[9]:
                print(f"Player{game[7]} has won")
        if game[3] == game[5] and game[5] == game[7]:
            print(f"Player{game[3]} has won")
    def __init__(self):
        self.exercise26()
def main():
    exercise26 = exercise_26()
if __name__ == '__main__':
    print(main())


