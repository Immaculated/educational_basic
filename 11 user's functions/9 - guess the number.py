import random

def randgen():
    rangen = random.randint(1, 10)
    return checking_numbas(rangen)
    
def checking_numbas(rangen):
    user = user_entering()
    if rangen > user:
        print('number is higher')
        return checking_numbas(rangen)
    elif rangen < user:
        print('number is lower')
        return checking_numbas(rangen)
    else:
        return play_again()

def user_entering():
    return int(input('Enter the number:\n'))
                
def play_again():
    answer = input('Bingo! Lets play again? y/n?\n')
    if answer == 'y':
        print('Ok, lets go again!')
        return randgen()
    elif answer == 'n':
        return print('See ya lata!')

randgen()