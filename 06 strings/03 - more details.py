text = input('enter the text\n')
link = '<a href=#> Подробнее</a>'
if len(text) > 100:
    print(text[:100] + str(link))
else:
    print('text is fine')