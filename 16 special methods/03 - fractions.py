# Реализовать класс рациональных чисел, т.е. множества чисел вида:
# ℚ={𝑚𝑛,где 𝑚∈ℤ,𝑛∈ℕ} . Реализовать для объектов данного класса
# операции сравнения, арифметические операции, арифметические
# операции с целыми числами. Реализовать исключение при делении
# на ноль и метод строкового представления, например, 
# в виде пары чисел m/n.

class Rational_numbers:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        
    def __repr__(self):
        return f"m = {self.m}, n = {self.n}"
    
    def __lt__(self, other):
        if self.m / self.n < other.m / other.n:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self.m / self.n > other.m / other.n:
            return True
        else:
            return False
        
    def __le__(self, other):
        if self.m / self.n <= other.m/other.n:
            return True
        else:
            return False
        
    def __ge__(self, other):
         if self.m / self.n >= other.m/other.n:
            return True
         else:
            return False
        
    def __eq__(self, other):
        if  self.m / self.n == other.m / other.n:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if  self.m / self.n != other.m / other.n:
            return True
        else:
            return False
    
    def __mul__(self, other):
        if type(other) == int:
            self.mul = self.m * other
            return f"{self.mul}/{self.n}"
        if type(other) == float:
            numerator=other * 10000
            denominator = 10000
            our_num=(self.m * numerator) / (self.n * denominator)
            return round(our_num,4)
        
    
    def __truediv__(self, other):
        if other == 0:
            raise Exception("You cannot divide by zero")
        self.truediv = self.n * other
        answer=round(self.m / self.truediv,4)
        return f"{answer}"
    
    def __str__(self):
        return f'{self.m} / {self.n}'
    
first = Rational_numbers(5,6)
second = Rational_numbers(1,2)
print(first)
print(first / 0)
print(first < second)
print(first > second)
print(first <= second)
print(first >= second)
print(first == second)
print(first != second)
print(first * 2.44)
print(str(first))