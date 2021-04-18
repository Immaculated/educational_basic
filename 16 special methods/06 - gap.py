# Разработать класс, описывающий математическое понятие
# промежуток  ((1;2),[2;5),(∞;−3]) . Реализовать операцию пересечения
# и разности, объединения, в теоретико-множественном смысле,
# если результат вновь является интервалом. Реализовать проверки
# на равенство и вхождение промежутков, кроме того,
# реализовать операцию проверки вхождения числа в промежуток.

class Gap:
    def __init__(self,x1,x2,first,second):
        self.x1 = x1
        self.x2 = x2
        self.first = first
        self.second = second
    
    def crossing(self,cross2):
        if self.x2 <= cross2.x2 and  self.x1 <= cross2.x1 or self.x2 <= cross2.x2 and  self.x1 <= cross2.x1
            print("inside")

first = Gap(-2,3,True,False)
second = Gap(-2,4,True,True)
first.crossing(second)