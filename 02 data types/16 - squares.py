n = float(input('enter length of rectangle\n'))
m = float(input('enter width of rectangle\n'))
k = float(input('enter side size of square\n'))
s1 = n * m # площадь прямоугольника
s2 = k ** 2 # площадь квадрата
number_of_cuts = int(s1 // s2)
print('number of squares that can be cut = ' + str(number_of_cuts))