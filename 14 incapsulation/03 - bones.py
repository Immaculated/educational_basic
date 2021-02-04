import random

class Bones:

    def __init__(self, name='bones'):
        self.name = name
        self.first = None
        self.second = None

    def roll(self):
        self.first = random.randint(1, 6)
        self.second = random.randint(1, 6)
        
    def count(self):
        return self.first + self.second
        
    def info(self):
        print(f'First bone - {self.first}, Second bone - {self.second}, Count - {self.count()}')
    
    def experiment(self, rolls, target):
        cnt = 0
        for _ in range(rolls):
            self.roll()
            if self.count() == target:
                cnt += 1
        return cnt/rolls      

bones = Bones()
bones.roll()
bones.count()
bones.info()
print(bones.experiment(1567, 5))