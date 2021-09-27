def main(number):
    """
    Ask the user for a number.
    Depending on whether the number is even or odd,
    print out an appropriate message to the user.
    """
    try:
        number = int(number)
    except:
        print("Your number is not an integer")
        return "not an integer"
    else:
        remainder = number%2
        if remainder == 0:
            print("Your number is even")
            return "even"
        elif remainder == 1:
            print("Your number is odd")
            return "odd"
def exercise2a(number_string):
    """If the number is a multiple of 4,
    print out a different message."""
    try:
        number = int(number_string)
    except:
        print("Your number is not an integer")
        return "not an integer"
    else:
        remainder = number%4
        if remainder == 0:
            print("Your number is divisible by 4")
            return "divisible by 4"
        elif remainder in [1,2,3]:
            print("Your number isn't divisible by 4")
            return "not divisible by 4"






if __name__ == '__main__':
    response = main(number="8")
    assert response == "even"

    assert main(number="7.5") == "not an integer"

    assert main(number="7") == "odd"


