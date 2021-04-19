# Десять классов школы, c 1 по 11, три месяца подряд собирали макулатуру,
# за каждый месяц известно количество килограммов, собранных каждым классом.
# Три массива формы (10,1).
# Найти:
# 1)суммарное количество собранной школой макулатуры,
# 2)количество собранной каждым классом макулатуры,
# 3)среднее количество макулатуры за каждый месяц.
# Если известна стоимость одного кг., найти:
# 4)сумму заработка за каждый месяц;
# 5)максимальную сумму набранную каким-либо классом за один месяц;
# 6)среднюю сумму по каждому классу.
# 7)Найти количество классов, собравших макулатуры меньше среднего значения.
# 8)Найти величину наибольшего прогресса в последний месяц, по сравнению с предыдущим
# указание: Три массива объединить в один,
# затем использовать операции библиотеки numpy.

import numpy as np
# inputting data
kg = int(input('enter max quantity of kilograms \n')) # max kg quantity for rnd
price = int(input('enter price of 1 kg \n')) # price
# generating and reshaping massives with kgs of paper
month1 = np.random.randint(1, kg, (10, 1)) # rnd month1
month2 = np.random.randint(1, kg, (10, 1)) # rnd month2
month3 = np.random.randint(1, kg, (10, 1)) # rnd month3
stacked = np.dstack([month1, month2, month3]) # new massive of 3 prev
table_with_data = stacked.reshape(10, 3) # reshaping in new massive
# quantities of kgs calculations(1-3 points)
total = int(np.sum(table_with_data)) # 1) sum of all collected paper
collected_by_every_class_at_all_time = table_with_data.sum(axis=1) # 2) collected by every class at all time
total_kg_per_month_by_all_classes = table_with_data.sum(axis=0) # total kg per month by all classes
even_quantity_of_paper_per_every_month = int(total_kg_per_month_by_all_classes.sum() / 3) # 3)even quantity of paper per every month
# with price calculations(4-6 points)
sum_of_getting_money_per_every_month = total_kg_per_month_by_all_classes * price # 4)sum of getting money per every month
max_money_per_month_by_someone_class = np.amax(table_with_data, axis=0) * price # 5)max money per month by someone class
even_sum_from_each_class = np.around((collected_by_every_class_at_all_time / 3) * price) # 6)even sum from each class
# comparisons(7-8 points)
quantity_of_classes_collected_low_than_mean = 0 # 7) quantity of classes collected low than mean
even_number_of_collected_paper = np.sum(collected_by_every_class_at_all_time) / len(collected_by_every_class_at_all_time) # for next step
for i in range(len(collected_by_every_class_at_all_time)):
    if collected_by_every_class_at_all_time[i] < (even_number_of_collected_paper):
        quantity_of_classes_collected_low_than_mean += 1
difference_list_1 = list()
difference_list_2 = list()
for i in range(len(table_with_data)): # 8)max progress between
    difference_list_1.append(month2[i] - month1[i])
    difference_list_2.append(month3[i] - month2[i])
progress1 = max(difference_list_1)
progress2 = max(difference_list_2)
# print all
print('table with data :\n', table_with_data)
print('total paper collected by all classes for 3 month : ', total)
print('collected by every class at all time : ', collected_by_every_class_at_all_time)
print('total kg per month by all classes : ', total_kg_per_month_by_all_classes)
print('even quantity of paper per every month : ', even_quantity_of_paper_per_every_month)
print('sum of getting money per every month : ', sum_of_getting_money_per_every_month)
print('max money per month by someone class : ', max_money_per_month_by_someone_class)
print('even sum from each class : ', even_sum_from_each_class)
print('even number of collected paper : ', even_number_of_collected_paper)
print('quantity of classes collected low than mean : ', quantity_of_classes_collected_low_than_mean)
print('max progress between 1st and 2nd months is : ', progress1)
print('max progress between 2nd and 3rd months is : ', progress2)