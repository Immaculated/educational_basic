rate_list = {'Vasya': 165, 'Daniel': 45, 'Jesus': 94, 'Hitler' : 25}
for key, value in rate_list.items():
        if value > 100:
            rate_list[key] = 100
print(rate_list)