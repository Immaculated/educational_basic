a, b, c = map(int, input('enter the 3 integer numbers\n').split())
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print('yes, at least one number is even')
else:
    print('no, all numbers are odd')