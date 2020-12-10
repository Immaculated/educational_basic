n = None
maxx = 0
while n != 0:
    n = float(input('enter as many numbers as you want\n'))
    if n > maxx:
        maxx = n
print('max element = ' + str(maxx))