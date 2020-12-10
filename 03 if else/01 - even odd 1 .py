def zero_equals_one_with_fabs():
    from math import fabs
    number = int(input('enter the integer number\n'))
    print(int(fabs(number % 2 - 1)))
zero_equals_one_with_fabs()

def zero_equals_one_with_not():
    number = int(input('enter the integer number\n'))
    print(int(not number % 2))
zero_equals_one_with_not()