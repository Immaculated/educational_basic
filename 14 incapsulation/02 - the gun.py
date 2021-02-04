import math

class Gun:

    def __init__(self, name='The gun'):
        self.name = name

    def distance(self, v, a):
        return ((v ** 2) * math.sin(2 * ((a * math.pi) / 180))) / 9.81

    def height(self, v, a):
        return ((v ** 2) * (1 - math.cos(2 * ((a * math.pi) / 180))) / 2) / (2 * 9.81)

shot = Gun()
print('distance of shooting = ' + str(shot.distance(10, 30)))
print('max height = ' + str(shot.height(10, 30)))