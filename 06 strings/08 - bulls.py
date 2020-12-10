word_1 = input('enter the first word:\n')
word_2 = input('enter the second word:\n')
count = 0
if len(word_1) == len(word_2):
    for char in range(len(word_1)):
        if word_1[char] == word_2[char]:
            count += 1
else: 
    print('check length of words')
print('quantity of coincident letters is: ' + str(count))