n = int(input('enter n\n'))
f = 1
if 0 <= n <= 1:
    f = 1
for i in range(2, n + 1):
    f *= i
print('factorial = ' + str(f))