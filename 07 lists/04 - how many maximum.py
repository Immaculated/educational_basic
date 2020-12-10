import random
random_list = []
for i in range(0,15):
    n = random.randint(1,9)
    random_list.append(n)
print(random_list)
max_of_list = [index for index, number in enumerate(random_list) if number == max(random_list)]
print('quantity of max elements in list = ' + str(len(max_of_list)))