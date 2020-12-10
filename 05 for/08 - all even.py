e = 0 
n = int(input('enter n number\n'))
print('enter ' + str(n) + ' integer numbers one by one\n')
for i in range(1, n + 1):
    m = int(input())
    if m % 2 == 0:
        e += 1
if e == n: print('all numbers are even')
else: print('not today')