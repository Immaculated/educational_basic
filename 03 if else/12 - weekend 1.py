day_of_week = int(input('enter the day of week\n'))
if day_of_week in range(0, 7):
    if 0 <= day_of_week <= 4:
        print('this is an ordinary weekday')
    else:
        print('this is weekend, we must drink vodka all the time')
else:
    print('check entering numbers')