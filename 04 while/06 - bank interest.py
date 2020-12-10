x = int(input('how much money did you put in the bank?\n'))
p = int(input('percents\n'))
y = int(input('minimum quantity of money through years\n'))
years = 0
while x < y:
    x = int((x * (1 + p / 100)) * 100) / 100
    years += 1
print('enough money will be in ' + str(years) + ' years')