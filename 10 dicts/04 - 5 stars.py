rate_list = {'Vasya': 65, 'Daniel': 45, 'Jesus': 94, 'Hitler' : 25}
name = 'Hitler'
stars_0, stars_1, stars_2, stars_3, stars_4, stars_5 = ' ', '*', '**', '***', '****', '*****'
if rate_list[name] < 20:
    print(stars_0)
elif 20 <= rate_list[name] < 40:
    print(name, str(stars_1))
elif 40 <= rate_list[name] < 60:
    print(name, str(stars_2))
elif 60 <= rate_list[name] < 80:
    print(name, str(stars_3))
elif 80 <= rate_list[name] < 100:
    print(name, str(stars_4))
elif rate_list[name] == 100:
    print(name, str(stars_5))