def exercise3(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
    """Take a list and write a program that prints out
    all the elements of the list that are less than 5."""
    for number in a:
        if number < 5:
            return number
def exercise3a(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
    """Instead of printing the elements one by one,
    make a new list that has all the elements less than 5
    from this list in it and print out this new list."""
    less_than_5 = []
    for number in a:
        if number < 5:
            less_than_5.append(number)
    print(less_than_5)
    return less_than_5
def exercise3b(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
    """Write this in one line of Python."""
    return [number for number in a if number < 5]
def exercise3c(b, a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
    """Ask the user for a number and return a list that contains only
    elements from the original list a that are smaller than that number
    given by the user."""
    number_list = []
    for number in a:
        if number < int(b):
            number_list.append(number)
    return number_list
if __name__ == '__main__':
    print(exercise3b())