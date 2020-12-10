word = input('enter the word\n')
if len(word) <= 7:
    print(word)
else:
    changed_word = [word[:4], '-', (word[-1:-3:-1])[::-1]]
    print(''.join(changed_word))