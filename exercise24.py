class exercise24(object):
    def problem_24(self):
        b = self.b
        x = ""
        b = int(b)
        b1 = b+1
        a = "__|"
        c = "___"
        x = x + str(b*c+"_\n")
        for y in range(b):
            x = str(x) + ("|" + b*a) + "\n"
        #    print(b*c+"-")
        self.x = x
    def __init__(self):
        b = input("How many rows/columns do you want?")
        self.b = b
        self.problem_24()

def main():
    exercise_24 = exercise24()
    print(exercise_24.x)
if __name__ == '__main__':
    main()