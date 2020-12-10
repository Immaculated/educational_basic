abc_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
text_set = set(input('enter the text: '))
symbols_count = text_set.intersection(abc_set)
print('there are ' + str(len(symbols_count)) + ' uniq symbols in this word, ' + 'symbols are ' + str(symbols_count))