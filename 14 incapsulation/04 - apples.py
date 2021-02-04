class Apple:
    
    def __init__(self, point, radius, name='Apple'):
        self.name = name
        self.x, self.y = point
        self.radius = radius
        
    def set_point(self, point):
        self.x, self.y = point
        
    def set_radius(self, radius):
        self.radius = radius
        
    def get_point(self):
        return self.x, self.y 
        
    def get_radius(self):
        return self.radius
    
    def info(self):
        print(f'Name {self.name} Coorditates {self.x, self.y} Radius {self.radius}')

    def intersection(self, obj):
        d = (((self.x - obj.x) ** 2) + ((self.y - obj.y) ** 2)) ** 0.5
        return d < self.radius + obj.radius
        
                
orange = Apple([1, 1], 2, name='Orange')
apple = Apple([2, 2], 1) 

orange.set_point([-1, -2])
apple.set_radius(2)

print(orange.get_point())

apple.info()

print(orange.intersection(apple))