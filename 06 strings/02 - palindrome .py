word = input('enter the word\n')
palindrome = word[::-1] # оператор расширенного среза, чтобы ввести слово наоборот
if palindrome == word: print('Yes, this word is palindrome')
else: print('No, this word is not palindrome')