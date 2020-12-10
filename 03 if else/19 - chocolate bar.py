n = int(input('first size of chocolate\n'))
m = int(input('second size of chocolate\n'))
k = int(input('quantity of pieces\n'))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Yes, you can do it!')
else:
    print('No, u cant')