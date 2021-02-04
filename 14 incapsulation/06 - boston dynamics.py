class Robot:
    
    def __init__(self, x, y, orient=1, name='robot', battery_charge = 10):
        self.name = name
        self.x = x
        self.y = y
        self.orient = orient
        self.path = [(x, y)]
        self.battery_charge = battery_charge
        self.path_length = 0
        
    def step(self, stp):
        self.battery_charge -= stp
        if self.battery_charge >= 0:
            if self.orient == 0:
                self.x += stp
            elif self.orient == 1:
                self.y += stp
            elif self.orient == 2:
                self.x -= stp
            else:
                self.y -= stp   
            (self.path).append((self.x, self.y))
            self.path_length += stp 
        else:
            print('the battery is low')
          
    def rotate(self, orient):
        self.battery_charge -= 1
        if self.battery_charge >= 0:
            self.orient = orient
        else:
            print('the battery is low')
            
    def print_path(self):
        print(*(self.path))
          
    def relocation(self):
        x1, y1 = self.path[0]
        x2, y2 = self.path[-1]
        return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

r2d2 = Robot(x=4, y=6, orient=1)
r2d2.step(5)
r2d2.rotate(0)
r2d2.step(4)
r2d2.rotate(2)
r2d2.print_path()
print(r2d2.path_length)
print(r2d2.relocation())