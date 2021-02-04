# This dogshit code was shared from one of students and changed, next time i must check all
def sum_keys(xdiction):
    summ = 0
    for elem in xdiction:
        summ += xdiction[elem]
    return summ
dict_numbers = {
     "q":12,
     "w":12,
     "e":12,
     "r":12,
     "t":2,
     "y":3
    }

def check(func, xdiction, answer):
    try:
        if func(xdiction) == answer:
            return True
        else:
            return False
    except:
        return False
            
try:
    ans = check(max, dict_numbers, 50)
except(NameError) as er:
    print(f'Wrong name {er}')
except(TypeError) as er:
    print(f'Missed arguments {er}')
else:
    if ans:
        print('Test passed')
    else:
        print('Test failed')
finally:
    print('It was tested, it doesnt mean dat shit works fine or not')