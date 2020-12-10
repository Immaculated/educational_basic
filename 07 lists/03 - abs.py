starting_list = [i for i in range(-10, 11)]
print('starting list: ' + str(starting_list))
new_list = [abs(number) for number in starting_list]
print('ending abs list: ' + str(new_list))