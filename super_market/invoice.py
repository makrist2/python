import datetime


class Invoice:
    MARGIN_COEFFICIENT = 0.2

    def __init__(self, number, customer, product):
        self.customer = customer
        self.number = number
        self.product = product
        self.cost_price = product.cost_price
        self.date = datetime.datetime.now()
        self.price = self.cost_price * self.MARGIN_COEFFICIENT + self.cost_price
        self.income = self.price - self.cost_price
