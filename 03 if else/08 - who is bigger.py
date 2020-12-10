def who_is_bigger_if():
    a = int(input('enter first integer number\n'))
    b = int(input('enter second integer number\n'))
    if a > b:
        print('max number from 2 numbers is ' + str(a))
    if a <= b:
        print('max number from 2 numbers is ' + str(b))
who_is_bigger_if()

def who_is_bigger_math():
    a = int(input('enter first integer number\n'))
    b = int(input('enter second integer number\n'))
    max = ((a // b) * a + (b // a) * b) // (a // b + b // a)
    print('max number from 2 numbers is ' + str(max))
who_is_bigger_math()