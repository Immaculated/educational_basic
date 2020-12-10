a, b, c = map(int, input('enter the 3 integer numbers\n').split())
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print('yes, all numbers are even')
else:
    print('no, at least one number is odd')