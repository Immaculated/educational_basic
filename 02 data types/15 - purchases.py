n = int(input('enter the number of purchases\n'))
r = int(input('enter partially of the price in rubles only\n'))
k = int(input('enter partially of the price in cents only\n'))
total_price = n * (r * 100 + k)
rubles = total_price // 100
cents = total_price % 100
print('the price of this product is ' + str(rubles) + ' rubles and ' + str(cents) + ' cents')