def exercise7(numbers = [1,4,9,16,25,36,49,64,81,100]):
    """Take a list and write one line of code that makes a new list
    that contains only the even elements of the new list"""
    return [x for x in numbers if x % 2 == 0]
print(exercise7())
assert exercise7() == [4,16,36,64,100]