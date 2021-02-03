first_rate_list = {'Leonardo': 65, 'Simon': 45, 'Solomon': 0, 'Jesus': 100}
second_rate_list = {'Leonardo': 65, 'Raphael': 45, 'Michaelangelo': 0, 'Donatello': 100}
for frst in list(first_rate_list.keys()):
    for scnd in second_rate_list.keys():
        if frst == scnd:
            del first_rate_list[frst]
print(first_rate_list)