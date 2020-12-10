summ = 0
only_good_list = [i for i in range(-10, 11)]
for number in only_good_list:
    if number > 0:
        summ += number
print('sum of positive elements = ' + str(summ))