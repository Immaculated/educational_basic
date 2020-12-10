n = int(input('enter the number\n'))
if n > 1:
    for i in range(2, n + 1):
        if n % i == 0 and n != i and i != 1:
            print('number is composite')
            break
    else: print('number is simple')
else:
    print('number is one, zero or negative')