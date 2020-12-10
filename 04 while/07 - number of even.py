n = None
i = 0
while n != 0:
    n = float(input('enter as many numbers as you want\n'))
    if not n % 2:
        i += 1
print('quantity of even numbers = ' + str(i))