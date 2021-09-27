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




if __name__ == '__main__':
    response = main(number="8")
    assert response == "even"

    assert main(number="7.5") == "not an integer"

    assert main(number="7") == "odd"


