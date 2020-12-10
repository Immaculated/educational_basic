low, hi = 1, 31
even_day, odd_day = 120, 100
day_of_month = int(input("enter day of month\n"))
if day_of_month < low:
     print('Error. Minimal value must be 1')
elif day_of_month > hi:
     print('Error. Maximal value must be 31')
else:
    if day_of_month % 2 == 0:
        print("in this day were evacuated " + str(even_day) + " cars")
    else:
        print("in this day were evacuated " + str(odd_day) + " cars")