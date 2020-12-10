import random
random_list = []
index = 0
for i in range(0,15): # генерация несортированного списка
    n = random.randint(1,9)
    random_list.append(n)
element = int(input('enter the element\n'))
print('started list: ' + str(random_list))
random_list.sort() # сортировка
print('sorted list:  ' + str(random_list))
while index < len(random_list) and random_list[index] <= element: # движение по списку, пока текущие значения <= элемента
    index += 1
random_list.insert(index, element) # inserting элемента на своё место по индексу, который был отслежен
print('new list:     ' + str(random_list))