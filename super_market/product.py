class Product:
    def __init__(self, category, cost_price, title):
        self.cost_price = cost_price
        self.category = category
        self.title = title


class Clothing(Product):
    def __init__(self, cost_price, size, title):
        super().__init__("Clothing", cost_price, title)
        self.size = size


class Food(Product):
    def __init__(self, cost_price, title, expiration):
        super().__init__("Food", cost_price, title)
        self.expiration = expiration


class Misc(Product):
    def __init__(self, cost_price, title):
        super().__init__("Misc", cost_price, title)