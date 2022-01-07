game = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
for x in range(9):
            a = input("What row do you want to put x in?")
            b = input("What column do you want to put x in?")
            a = int(a)
            b = int(b)
            for x in range(3):
                if x == a:
                    for y in range(3):
                        if y == b:
                            game[x][y] = "x"
            print(game[0])
            print(game[1])
            print(game[2])
            c = input("What row do you want to put o in?")
            d = input("What column do you want to put o in?")
            c = int(c)
            d = int(d)
            if game[0][0] == game[0][1]:
                if game[0][0] == game[0][2]:
                    print(f"Player{game[0][0]} has won")
                    exit()
            if game[0][0] == game[1][0]:
                if game[0][0] == game[2][0]:
                    print(f"Player{game[0][0]} has won")
                exit()
            if game[0][0] == game[1][1]:
                if game[0][0] == game[2][2]:
                    print(f"Player{game[0][0]} has won")
                exit()
            if game[1][0] == game[1][1]:
                if game[1][1] == game[1][2]:
                    print(f"Player{game[4]} has won")
                    exit()
            if game[0][1] == game[1][1]:
                if game[0][1] == game[2][1]:
                    print(f"Player{game[0][1]} has won")
                    exit()
            if game[0][2] == game[1][2]:
                if game[0][2] == game[2][2]:
                    print(f"Player{game[0][2]} has won")
                    exit()
            if game[2][0] == game[2][1]:
                if game[2][0] == game[2][2]:
                    print(f"Player{game[2][0]} has won")
                    exit()
            if game[0][2] == game[1][1] and game[0][2] == game[2][0]:
                print(f"Player{game[0][2]} has won")
                exit()
            for x in range(3):
                if x == c:
                    for y in range(3):
                        if y == d:
                            game[c][d] = "o"
            print(game[0])
            print(game[1])
            print(game[2])
            if game[0][0] == game[0][1]:
                if game[0][0] == game[0][2]:
                    print(f"Player{game[0][0]} has won")
                    exit()
            if game[0][0] == game[1][0]:
                if game[0][0] == game[2][0]:
                    print(f"Player{game[0][0]} has won")
                exit()
            if game[0][0] == game[1][1]:
                if game[0][0] == game[2][2]:
                    print(f"Player{game[0][0]} has won")
                exit()
            if game[1][0] == game[1][1]:
                if game[1][1] == game[1][2]:
                    print(f"Player{game[4]} has won")
                    exit()
            if game[0][1] == game[1][1]:
                if game[0][1] == game[2][1]:
                    print(f"Player{game[0][1]} has won")
                    exit()
            if game[0][2] == game[1][2]:
                if game[0][2] == game[2][2]:
                    print(f"Player{game[0][2]} has won")
                    exit()
            if game[2][0] == game[2][1]:
                if game[2][0] == game[2][2]:
                    print(f"Player{game[2][0]} has won")
                    exit()
            if game[0][2] == game[1][1]
                if game[0][2] == game[2][0]:
                    print(f"Player{game[0][2]} has won")
                    exit()