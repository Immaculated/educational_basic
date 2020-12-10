n1 = int(input('enter the natural two-digit number\n'))
if n1 in range(10,100):
    print('number of tens in this number is ' + str(n1 // 10 % 10))
else:
    print('Error! the number must be in range from 10 to 99')
