rate_list = {'Vasya': 65, 'Daniel': 45, 'Jesus': 94, 'Hitler' : 25}
count = 0
for key in sorted(rate_list, key=rate_list.get):
    print(key, '\t', rate_list[key])
    count += rate_list[key]
avegrage_rating = count / len(rate_list)
print('average rating ' + str(avegrage_rating))