c = int(input('enter the price in cents \n'))
r = c // 100
k = c % 100
print('the price of this product is ' + str(r) + ' rubles and ' + str(k) + ' cents')