t = int(input('enter quantity of hours\n'))
if t % 10 == 1 and (t % 100) != 11:
    print(str(t) + ' час')
elif (2 <= t % 10 <= 4) and ((t % 100) not in range(12, 15)):
    print(str(t) + ' часа')
else :
    print(str(t) + ' часов')