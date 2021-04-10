class figure:
    
    def __init__(self, X0, Y0):   # coords
        self.x0 = X0
        self.y0 = Y0

class triangle(figure):
    
    def __init__(self, A, B, C):  # triangle with sides
        self.a = A
        self.b = B
        self.C = C
        
    def square(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    
class rectangle(figure):
    
    def __init__(self, A, B):  # rectangle with sides
        self.a = A
        self.b = B
        
    def square(self):
        return self.a * self.b
        
class circle(figure):
    
    def __init__(self, R):    # circle with radius
        self.r = R
        
    def square(self):
        import math
        return math.pi * self.r ** 2
