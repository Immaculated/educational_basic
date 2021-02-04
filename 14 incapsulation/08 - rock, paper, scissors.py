import random

class RockScissorsPaper:

    def __init__(self):
        self.sequence = ('rock', 'scissors', 'paper')
        self.rnd_num = None
        self.answer = None
     
    def set_answer(self):
        self.rnd_num = random.choice(self.sequence)
        self.answer = input('Enter rock or scissors or paper: ')
        
    def check_winner(self):
        if self.rnd_num == self.answer:
            print('Try again')
        elif self.rnd_num == 'rock':
            if self.answer == 'scissors':
                print('U lose')
            else:
                print('U win')
        elif self.rnd_num == 'scissors':
            if self.answer == 'paper':
                print('U lose')
            else:
                print('U win')
        elif self.rnd_num == 'paper':
            if self.answer == 'rock':
                print('U lose')
            else:
                print('U win')
        

    def game_over(self):
        return self.rnd_num != self.answer

new = RockScissorsPaper()

while not new.game_over():
    new.set_answer()
    new.check_winner()
print('End!')