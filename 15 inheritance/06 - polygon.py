class Point:
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __str__(self):
        return f'({self.x}; {self.y})'
        
        
class Polygon:
    
    
    def __init__(self):
        self.points = []
    
    def add_point(self, point):
        self.points.append(point)
        
    def info(self):
        print(self.points)
        
    def is_equal(self, other_poly):
        pass

    
poly = Polygon()
poly.add_point(Point(0,0))
poly.add_point(Point(-1,0.5))
poly.add_point(Point(-1.5,1))
poly.add_point(Point(-0.5,2))
poly.add_point(Point(0,0.5))
poly.info()