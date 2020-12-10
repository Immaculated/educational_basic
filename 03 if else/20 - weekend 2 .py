n = int(input('choose day of order\n'))        
k = int(input('choose delivery time\n'))        
x = (k + n) % 7
if n in range(0, 7):
    if x == 5:
        x = (k + n + 2) % 7
        print('day of delivered is ' + str(x))
    elif x == 6:
        x = ((k + n + 1) % 7)
        print('day of delivered is ' + str(x))
    else:
        print('day of delivered is ' + str(x))
else:
    print('do u have more than 7 days of week? really?')