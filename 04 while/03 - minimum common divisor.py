n = int(input('enter the integer number\n'))
i = 2 # на 1 смысла делить нет, так как заданное число не меньше 2
while n % i != 0: # когда разделится без остатка, цикл прекратится
    i += 1
print('minimum common divisor = ' + str(i))