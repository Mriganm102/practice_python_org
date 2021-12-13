def exercise27():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    a = input("What row do you want to put x in?")
    b = input("What column do you want to put x in?")
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
    print(game)


exercise27()