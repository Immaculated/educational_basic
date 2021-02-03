week = {
    1:'Monday', 
    2:'Tuesday', 
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
    }
number_of_day = int(input('Enter the day of week\n'))
if 1 <= number_of_day <= 5:
    print(str(week[number_of_day]) + ', Working day')
elif 6 <= number_of_day <= 7:
    print(week[number_of_day])
else:
    print('There are only 7 days of week')