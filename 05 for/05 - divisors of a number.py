n = int(input('enter natural number\n'))
print('divisors of number ' + str(n) + ' are: ')
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
        i += 1