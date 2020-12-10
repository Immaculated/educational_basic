import random
user = None
generation = random.randint(0, 10)
while generation != user:
    while True:
        user = int(input('enter the number: '))
        if generation > user: print('number is higher')
        elif generation < user: print('number is lower')
        else:
            print('bingo!')
            answer = input('lets play again? Y/N?\n')
            if answer == 'Y':
                print('ok lets go again')
            elif answer == 'N':
                print('bye!bye! see ya lata!')
                break