rate_list = {'Vasya':65, 'Daniel':45} 
name = 'Daniel'
if name in rate_list.keys():
    rate_list[name] += 1
else:
    rate_list.setdefault(name, 0)
print(rate_list)