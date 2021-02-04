import random
import pickle

def w_file(data, fname):
    with open(fname, "wb") as file:
        pickle.dump(data, file)

def r_file(fname):
    with open(fname, "rb") as file:
        results = pickle.load(file)
        return results

def field_of_dreams():
    question, word = random.choice(list(r_file('words.data').items()))
    print('Задание: ', question)
    attempt = ''                    
    field = '*' * len(word)
    while field != word and attempt != word:
        attempt = input('Enter the letter or the word: \n')
        if attempt != word and attempt in word:
            plase_in_field = ''
            for please in range(len(word)):
                if attempt == word[please]:
                    plase_in_field += attempt
                elif attempt != word[please]:
                    plase_in_field += field[please]
            field = plase_in_field
        print(field)
    print('Верно!')

words = {
'На свете есть много лягушек: все они очень разные. \
Свои названия они получили за свою внешность: живёт в \
траве - травяная, с острой мордой - остромордая, живёт в пруду - прудовая.\
А эта африканская лягушка получила своё название за необычный рот.\
Как зовут эту лягушку?':'узкорот',
' Эта птица может ходить по дну водоёма, похожа на воробья. Её так и прозвали\
«водяной воробей». Что это за птица?':'оляпка',
'На морском дне растёт очень опасная водоросль: актиния – она больно жжётся. \
А эта рыбка дружит с ней. И наряд у этой рыбки яркий, весёлый, пёстрый. \
Что это за рыбка?':'клоун'
}

w_file(words, 'words.data')
field_of_dreams()