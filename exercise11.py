def prime(n):
    if n<=1:
        print("Prime")
    if n==2:
        print("Prime")
    for x in range(2,n):
        if n%x == 0:
            print("Not Prime")
        else:
            print("Prime")
prime(4)