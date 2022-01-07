class exercise29(object):
    def exercise27(self):
        game = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        for x in range(9):
            def x_marking():
                a = input("What row do you want to put x in?")
                b = input("What column do you want to put x in?")
                a = int(a)
                b = int(b)
                for x in range(3):
                    if x == a:
                        for y in range(3):
                            if y == b:
                                if game[x][y] == "x" or game[x][y] == "o":
                                    print("That spot has already been marked")
                                    x_marking()
                                else:
                                    game[x][y] = "x"
            x_marking()
            print(game[0])
            print(game[1])
            print(game[2])
            if game[0][0] == game[0][1]:
                if game[0][0] == game[0][2]:
                    return (f"Player {game[0][0]} has won")
                    exit()
            if game[0][0] == game[1][0]:
                if game[0][0] == game[2][0]:
                    return (f"Player {game[0][0]} has won")
                    exit()
            if game[0][0] == game[1][1]:
                if game[0][0] == game[2][2]:
                    return (f"Player {game[0][0]} has won")
                    exit()
            if game[1][0] == game[1][1]:
                if game[1][1] == game[1][2]:
                    print(f"Player {game[4]} has won")
                    exit()
            if game[0][1] == game[1][1]:
                if game[0][1] == game[2][1]:
                    print(f"Player {game[0][1]} has won")
                    exit()
            if game[0][2] == game[1][2]:
                if game[0][2] == game[2][2]:
                    print(f"Player {game[0][2]} has won")
                    exit()
            if game[2][0] == game[2][1]:
                if game[2][0] == game[2][2]:
                    print(f"Player {game[2][0]} has won")
                    exit()
            if game[0][2] == game[1][1] and game[0][2] == game[2][0]:
                print(f"Player {game[0][2]} has won")
                exit()
            def o_marking():
                c = input("What row do you want to put o in?")
                d = input("What column do you want to put o in?")
                c = int(c)
                d = int(d)
                for x in range(3):
                    if x == c:
                        for y in range(3):
                            if y == d:
                                if game[x][y] in ["x", "o"]:
                                    print("That spot has already been marked")
                                    o_marking()
                                else:
                                    game[x][y] = "o"
            o_marking()
            print(game[0])
            print(game[1])
            print(game[2])
            if game[0][0] == game[0][1]:
                if game[0][0] == game[0][2]:
                    print(f"Player {game[0][0]} has won")
                    exit()
            if game[0][0] == game[1][0]:
                if game[0][0] == game[2][0]:
                    print(f"Player {game[0][0]} has won")
                    exit()
            if game[0][0] == game[1][1]:
                if game[0][0] == game[2][2]:
                    print(f"Player {game[0][0]} has won")
                    exit()
            if game[1][0] == game[1][1]:
                if game[1][1] == game[1][2]:
                    print(f"Player {game[4]} has won")
                    exit()
            if game[0][1] == game[1][1]:
                if game[0][1] == game[2][1]:
                    print(f"Player {game[0][1]} has won")
                    exit()
            if game[0][2] == game[1][2]:
                if game[0][2] == game[2][2]:
                    print(f"Player {game[0][2]} has won")
                    exit()
            if game[2][0] == game[2][1]:
                if game[2][0] == game[2][2]:
                    print(f"Player {game[2][0]} has won")
                    exit()
            if game[0][2] == game[1][1] and game[0][2] == game[2][0]:
                print(f"Player {game[0][2]} has won")
                exit()
    def __init__(self):
        print(self.exercise27())
def main():
    e29 = exercise29()
if __name__ == '__main__':
    main()
