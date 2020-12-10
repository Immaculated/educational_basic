a, b, c = map(float, input('enter lengths of 3 line segments\n').split())
if b <= a >= c:
    print('max is ' + str(a))
elif a <= b >= c:
    print('max is ' + str(b))
else:
    print('max is ' + str(c))