n = int(input('enter the integer number\n'))
two = 2
index = 1
while two <= n:
    two *= 2
    index += 1 
    print('index = ' + str(index - 1) + ',' + ' two in index = ' + str(two // 2))