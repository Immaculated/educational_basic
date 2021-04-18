# Разработать класс, описывающий математическое понятие интервал
# и операции над ним (интервальную арифметику).

class Interval:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __repr__(self):
        return f"a = {self.a},b = {self.b}"
    
    def __add__(self, other):
        sum_ac = self.a + other.a
        sum_bd = self.b + other.b
        return f"[{sum_ac},{sum_bd}]"
    
    def __sub__(self, other):
        sub_ad = self.a - other.b
        sum_bc = self.b - other.a
        return f"[{sub_ad},{sum_bc}]"
    
    def __mul__(self, other):
        mul_a = round(min(self.a * other.a,self.a * other.b,self.b * other.a,self.b * other.b),4)
        mul_b = round(max (self.a * other.a,self.a * other.b,self.b * other.a,self.b * other.b),4)
        return f"[{mul_a},{mul_b}]"
    
    def __truediv__(self, other):
        tr_a =round(min(self.a / other.a,self.a / other.b,self.b / other.a,self.b / other.b),4)        
        tr_b = round(max (self.a / other.a,self.a / other.b,self.b / other.a,self.b / other.b),4)
        return f"[{tr_a},{tr_b}]"

first_ = Interval(1,7)
second_ = Interval(-9,15)
print(first_)
print(first_ + second_)
print(first_ - second_)
print(first_ * second_)
print(first_ / second_)