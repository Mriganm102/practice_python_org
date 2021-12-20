class exercise28(object):
    def exercise_28(self):
        first_number = self.first_number
        second_number = self.second_number
        third_number = self.third_number
        first_number = int(first_number)
        second_number = int(second_number)
        third_number = int(third_number)
        if first_number > second_number and first_number > third_number:
            final_statement = f"{first_number} is bigger than {second_number} and {third_number}"
        if second_number > first_number and second_number > third_number:
            final_statement = f"{second_number} is bigger than {first_number} and {third_number}"
        if third_number > second_number and third_number > first_number:
            final_statement = f"{third_number} is bigger than {second_number} and {first_number}"
        self.final_statement = final_statement
    def __init__(self):
        first_number = input("What is the first number?")
        second_number = input("What is the second number?")
        third_number = input("What is the third number?")
        self.first_number = first_number
        self.second_number = second_number
        self.third_number = third_number
        self.exercise_28()
def main():
    e28 = exercise28()
    print(e28.final_statement)
if __name__ == '__main__':
    main()