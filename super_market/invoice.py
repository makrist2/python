import datetime
VALUE = 20


class Invoice:
    def __init__(self, number, customer, product):
        self.customer = customer
        self.number = number
        self.product = product
        self.cost_price = product.cost_price
        self.date = datetime.datetime.now()
        self.price = (self.cost_price * VALUE / 100) + self.cost_price
        self.income = self.price - self.cost_price
