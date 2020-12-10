temp = list(map(float, input('enter the temperatures\n').split(' ')))
average = round(sum(temp)/len(temp), 1) # совсем слегка округлим xD
print('average value of temp = ' + str(average))