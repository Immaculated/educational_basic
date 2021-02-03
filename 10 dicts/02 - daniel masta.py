rate_list = {'Vasya':65, 'Daniel':45} 
name = 'Daniel'
if rate_list[name] < 31:
    print(name + ' (Noob)')
elif 31 <= rate_list[name] < 61:
    print(name + ' (Masta)')
elif 61 <= rate_list[name]:
    print(name + ' (Grandmaster)')