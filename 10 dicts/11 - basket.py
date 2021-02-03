cart = {
    1 : {'name':'Drugs', 'price':1200, 'count':2},
    12 : {'name':'Guns', 'price':1100, 'count':6},
    3 : {'name':'People', 'price':5400, 'count':1}, # Creating basic dict of dict with keys-values
}
sorted_dict = sorted(
    cart, 
    key=lambda key: cart[key]['price'] * cart[key]['count'], # Creating a sorted dict with lambda func by multiplying key-values
    reverse=True
)
for key in sorted_dict:
    print(
        cart[key]['name'], 
        'price =', 
        cart[key]['price'] * cart[key]['count']
    )