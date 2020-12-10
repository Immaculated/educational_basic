t = int(input('what is the temperature today?\n'))
if t < -30:
    print('stay home!')
elif -30 <= t < -10:
    print('today is cold')
elif -10 <= t < +5:
    print('today is not cold')
elif +5 <= t < +15:
    print('today is warm')
elif +15 <= t < +25:
    print('today is very warm')
elif +25 <= t < +35:
    print('today is hot')
elif t >= +35:
    print('scorching heat!')