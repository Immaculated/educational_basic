class Product:
    
    def __init__(self):
        self.list_of_product = {}
        
    def product_adding(self, new_product, new_price):
        self.list_of_product[new_product] = new_price
        
    def get_price(self, name_of_product):
        return self.list_of_product[name_of_product]
    
class Order(Product):
    
    def __init__(self, product, time_of_order, client_name, address_of_client):
        self.time = time_of_order
        self.name = client_name
        self.address = address_of_client
        self.list_of_purchase = {}
        self.list_of_product = list_of_product
        
    def purchase_adding(self, adding_product):
        if adding_product in self.list_of_purchase:
            self.list_of_purchase[adding_product] += 1
        else:
            self.list_of_purchase[adding_product] = 1
            
    def purchase_deleting(self, deleting_product):
        if deleting_product in self.list_of_purchase:
            if self.list_of_purchase[deleting_product] > 1:
                self.list_of_purchase[deleting_product] -= 1
            else:
                del self.list_of_purchase[deleting_product]
        else:
            print('Такого продукта нет в заказе')
            
    def cost_of_order(self):
        sum = 0
        for key in self.list_of_purchase:
            sum += self.list_of_purchase[key] * self.list_of_product[key]
        return sum
    
    def info(self):
        print("Клиент", self.name, " состав заказа:")
        for i in self.list_of_purchase:
            print('Товар ', i, ' количеством ', self.list_of_purchase[i], ' шт.', )
        print('Стоимость:', self.cost_of_order())
        print('Адрес доставки:', self.address)
        print('Время создания заказа:', self.time)
                   
assortiment = product()
assortiment.product_adding('телевизор', 20000)
assortiment.product_adding('стол',5000)
assortiment.product_adding('холодильник',50000)


from datetime import datetime
example = order(assortiment, datetime.now(), 'Вася', 'Моссковское шоссе, 1')
example.purchase_adding('телевизор')
example.purchase_adding('телевизор')
example.purchase_adding('телевизор')
example.purchase_deleting('телевизор')
example.purchase_adding('холодильник')

example.info()