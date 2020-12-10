dictionary = 'AGTC'
word = input('enter the word\n')
for char in word:
    if char not in dictionary:
        print('word is not compatible')
        break
else:
    print('word is fine')