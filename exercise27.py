class exercise_27():
    def exercise27(self):
        a = self.a
        b = self.b
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        a = int(a)
        b = int(b)
        for x in range(3):
            if x == a:
                for y in range(3):
                    if y == b:
                        game[x][y] = "x"
        c = input("What row do you want to put o in?")
        d = input("What column do you want to put o in?")
        c = int(c)
        d = int(d)
        for x in range(3):
            if x == c:
                for y in range(3):
                    if y == d:
                        game[c][d] = "o"
        self.game = game
    def __init__(self):
        a = input("What row do you want to put x in?")
        b = input("What column do you want to put x in?")
        self.a = a
        self.b = b
        self.exercise27()

def main():
    e27 = exercise_27()
    print(e27.game)
if __name__ == '__main__':
    main()