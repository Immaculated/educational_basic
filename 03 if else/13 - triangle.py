a, b, c = map(float, input('enter lengths of 3 line segments\n').split())
if a + b > c and a + c > b and b + c > a:
    print('triangle exists')
else:
    print('triangle not exists')