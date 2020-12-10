a = int(input('enter the even number what u seeing on botside\n'))
if a % 2 == 0 and a != 0:
    b = int(input('enter the even number what u seeing on topside\n'))
else:
    print('are u retarded? you cant count')
if b % 2 != 0 and b != 0:
    print('are u retarded? you cant count')
else:
    if a < b and a % 2 == 0 and b % 2 == 0:
        print('there are ' + str((b - a) * 2) + ' cabins on the Ferris wheel')
    else:
        print('you are lost, choose another amusement park')