rate_list = {'Vasya': 51, 'Daniel': 50, 'Jesus': 94, 'Hitler': 25}
stars_0, stars_1, stars_2, stars_3, stars_4, stars_5 = ' ', '*', '**', '***', '****', '*****'
for key, value in rate_list.items():
    if rate_list[key] < 31:
        print(key + ' (Noob)', end='')
    elif 31 <= rate_list[key] < 61:
        print(key + ' (Masta)', end='')
    elif 61 <= rate_list[key]:
        print(key + ' (Grandmaster)', end='')
    if rate_list[key] < 20:
        print(stars_0)
    elif 20 <= rate_list[key] < 40:
        print(str(stars_1))
    elif 40 <= rate_list[key] < 60:
        print(str(stars_2))
    elif 60 <= rate_list[key] < 80:
        print(str(stars_3))
    elif 80 <= rate_list[key] < 100:
        print(str(stars_4))
    elif rate_list[key] == 100:
        print(str(stars_5))