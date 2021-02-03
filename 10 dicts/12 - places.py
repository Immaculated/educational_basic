starting_dict = {'Vasya': 65, 'Daniel': 12, 'Jesus': 45, 'Hitler': 45} # Starting dict
sorted_by_values_list = sorted(starting_dict, key=starting_dict.get, reverse=True) # Sorted by values dict in reverse position
list_of_standings = [] # New empty list for standings
values_list = sorted(starting_dict.values()) # Sorted dict values in new list
count = 1
for i in range(1, len(starting_dict)):
    if values_list[i-1] == values_list[i]:
        list_of_standings.append(count)
        count += 0
    else:
        list_of_standings.append(count)
        count += 1
release = dict(zip(sorted_by_values_list, list_of_standings))
print(starting_dict)
print(release)