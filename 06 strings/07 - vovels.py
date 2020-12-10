def vovels_count_with_lists():
    result = []
    word = input('enter the word\n')
    list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for char in word: # перебор букв слова
        if char in list_of_vowels and char not in result: # проверка, есть ли текущая буква слова в списке, и она не повторяется
            result.append(char)
    print('vowels letters in word ' + f'"{word}"' + ' are: '  + str(result))
vovels_count_with_lists()


def vovels_count_strings_only():
    result = ''
    word = input('enter the word\n')
    list_of_vowels = 'aeiouy'
    for char in word: # перебор букв слова
        if char in list_of_vowels and char not in result: # проверка, есть ли текущая буква слова в списке, и она не повторяется
            result += char + ', '
    print('vowels letters in word ' + f'"{word}"' + ' are: '  + str(result.rstrip(', ')))
vovels_count_strings_only()