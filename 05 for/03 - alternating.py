summ = 0
n = int(input('enter n\n'))
for i in range(1, n + 1):
    summ += (((-1) ** (i + 1)) / i)
print('sum of numbers = ' + str(summ))