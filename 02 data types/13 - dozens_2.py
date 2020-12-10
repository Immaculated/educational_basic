n1 = int(input('enter the natural number\n'))
if n1 <= 0:
    print('you did not study math well at school')
else:
    print('number of tens in this number is ' + str(n1 // 10 % 10))