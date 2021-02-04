import random

class GuessTheNumber:

    def __init__(self):
        self.rnd_num = random.randint(1, 10)
        self.answer = None
     
    def set_answer(self):
        self.answer = int(input('Enter the number:\n'))
        
    def check_winner(self):
        if self.rnd_num > self.answer:
            print('The number is higher')
        elif self.rnd_num < self.answer:
            print('The number is lower')

    def game_over(self):
        return self.rnd_num == self.answer

new = GuessTheNumber()

while not new.game_over():
    new.set_answer()
    new.check_winner()  
print('Bingo!')