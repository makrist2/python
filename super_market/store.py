class Store:

    def __init__(self, name):
        self.name = name
        self._items = []

    def __str__(self):
        return "%i %s" % (len(self._items), str(self._items))

    def add_item(self, item):
        self._items.append(item)

    def get_item(self):
        return self._items

    def remove_item(self, item):
        self._items.remove(item)