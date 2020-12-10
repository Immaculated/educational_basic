from random import shuffle
local_max_min_list = [i for i in range(10)]
shuffle(local_max_min_list)
max_list = []
min_list = []
print(local_max_min_list)
for i in range(1, len(local_max_min_list) - 1):
    if local_max_min_list[i - 1] < local_max_min_list[i] > local_max_min_list[i + 1 ]:
        max_list.append(local_max_min_list[i])
    elif local_max_min_list[i - 1] > local_max_min_list[i] < local_max_min_list[i + 1 ]:
        min_list.append(local_max_min_list[i])
print('local max in this list: ' + str(max_list))
print('local min in this list: ' + str(min_list))