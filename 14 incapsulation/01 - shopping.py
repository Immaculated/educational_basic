class Shopping:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def buy_cost(self, unit):
        if unit == 'usd':
            return ((self.price * 100) * self.quantity) // 100
        elif unit == 'cents':
            return (self.price * 100) * self.quantity
        else:
            return self.price * self.quantity

    def get_buy_cost(self, unit='usd.cents'):
        print(f'Buying {self.name} with price {self.price} usd and q. {self.quantity} with sum {self.buy_cost(unit)} {unit}.')
        
nuts = Shopping('Nuts', 42.53, 15)
nuts.get_buy_cost()