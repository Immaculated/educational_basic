n = None 
maxx = 0
mylist = [] 
print('enter as many numbers as you want')
while n != 0:
    n = int(input())
    mylist.append(n)
mylist.pop() # удаление нуля из списка
for i in range(1, len(mylist) - 1): # первый и последний элементы не могут быть максимумами, ноль не в массиве
    if mylist[i - 1] < mylist[i] > mylist[i + 1 ]: # проверка на локальный максимум без учёта плато
        maxx += mylist[i]
        i += 1 
print('mylist is ' + str(mylist))
print('sum of local max = ' + str(maxx))