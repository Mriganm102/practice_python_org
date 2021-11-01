def exercise13(number_of_elements_to_print):
    """
    Input = number_of_elements_to_print
    Pre-condition = The input has to be a positive integer
    Write a program that asks the user how many Fibonnaci
    numbers to generate and then generates them.
    Post_condition = The list has fibbonaci numbers and
    contains the input number of elements
    :return: The fibbonaci sequence with the input number of elements
    """
    number_of_elements_to_print = number_of_elements_to_print - 2
    f0 = 0
    f1 =1
    F = [f0, f1]
    for x in range(number_of_elements_to_print):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        F.append(f2)
    return F
print(exercise13(11))
