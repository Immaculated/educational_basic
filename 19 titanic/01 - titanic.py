import pandas as pd
df = pd.read_csv('titanic.csv', index_col='PassengerId')

"""Словарь данных

Survived (Выживание) 0 = Нет, 1 = Да,
Pclass: 1 = 1 класс, 2 = 2 класс, 3 = 3 класс
Sex: Пол
Age: Возраст в годах
SibSp: Количество братьев и сестер / супругов на борту Titanic
Parch: Количество родителей / детей на борту Titanic
Fare: цена билета
Embarked: Порт посадки C = Шербур, Q = Куинстаун, S = Саутгемптон

"""

# Выяснить процент выживших.
total_passengers = df["Survived"].count()
surviving_passengers = df[df.Survived == 1].Survived.count()
percent_of_survivals = surviving_passengers / total_passengers
print('total passengers: ', total_passengers)
print('surviving passengers: ', surviving_passengers)
print('percent of survivors: ', percent_of_survivals * 100)

# Сколько мужчин в выборке? Сколько из них спаслись?
quantity_of_mans = df[df.Sex == 'male'].Sex.count()
quantity_of_mans_survivers = df[(df.Sex == 'male') & (df.Survived == 1)].Sex.count()
print('mans in the selection: ', quantity_of_mans)
print('surviving mans: ', quantity_of_mans_survivers)

# Сколько лет самой пожилой спасенной женщине? Как её имя?
the_most_old_woman = df[(df.Sex == 'female') & (df.Survived == 1)].sort_values(by='Age', ascending=False)
print('the most old woman is: \n')
print(the_most_old_woman[:1][['Age','Name']])

# Сколько детей спаслось? (< 18 лет)
children_survivers = df[(df.Age < 18) & (df.Survived == 1)].Survived.count()
print('children survivers: ', children_survivers)

# Сколько женщин было в первом классе, сколько из них выжило?
total_women_in_first_class = df[(df.Sex == 'female') & (df.Pclass == 1)].Sex.count()
women_from_first_class_survivers = df[(df.Sex == 'female') & (df.Survived == 1) & (df.Pclass == 1)].Survived.count()
print('total womens in first class: ', total_women_in_first_class)
print('womens from first class are survivors: ', women_from_first_class_survivers)

# Найти общую стоимость всех билетов, и по каждому классу в отдельности, построить диаграмму.
import matplotlib.pyplot as plt

total_sum_of_tickets = df['Fare'].sum()
print('Total ticket price: ', total_sum_of_tickets)
group = df.groupby(['Pclass'])['Fare'].sum()
print(group)

plt.xlabel('Pclass')
plt.ylabel('ticket prices relative by class')
plt.bar(group.index, [group[1],group[2],group[3]], color='#9146ff', edgecolor='black', linewidth=1, hatch='//')
plt.show()