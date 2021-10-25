def prime(n):
    """
    N is the input
    Pre-condtion = n is either a prime or composite number
    Ask the user for a number
    and determine whether the number is prime or not.
    Post-condition = it prints out whether n was prime or composite
    """
    if n<1:
        print("Invalid")
    if n == 1:
        print("Prime")
    if n==2:
        print("Prime")
    for x in range(2,n):
        if n%x == 0:
            return ("Not Prime")
        else:
            print(f"Your number is not divisible by {x}")
    return "Prime"
print(prime(89))