# Encapsulation : Wrapping data and functions into single unit (object)

class Market:
    def __init__(self, item, price):
        self.item = item
        self.__price = price

    def show_item(self):
        print("Item:", self.item)
        print("Price:", self.__price)

    def update_price(self, price):
        self.__price = price


m1 = Market("Rice", 70)

m1.show_item()

m1.update_price(80)

print("After updating price:")
m1.show_item()