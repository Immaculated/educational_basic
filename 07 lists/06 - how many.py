import random
random_list = []
for i in range(0,15):
    n = random.randint(1,9)
    random_list.append(n)
print('number', 'quantity', sep= ' | ')
for number in random_list:
    quantity = random_list.count(number)
    print(' '*5 + f'{number} | {quantity}')