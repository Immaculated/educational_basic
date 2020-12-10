import random
q0 = 0 # счётчик числа нулей
q2 = 0 # счётчик числа двоек
i = 0 # счётчик числа генераций
mylist = []
while True: # бесконечный цикл
    n = random.randint(0, 2) # рэндом генератор
    i += 1 # считает генерации
    if n == 0: q0 += 1 # если генерируемый элемент = 0 , счётчик q0 += 1
    elif n == 1: pass # если 1, то ничего не делать
    else: q2 += 1 # если 2, то счётчик q2 += 1
    mylist.append(n)
    if q0 == q2: # если число нулей равно числу двоек, условие выполнено
        break # принудительный выход из бесконечного цикла
print('list of generated numbers is ' + str(mylist))
print('number of generations = ' + str(i))
print('quantity of zeros and twos is ' + str(q0) + ' and ' + str(q2) + ' of each')