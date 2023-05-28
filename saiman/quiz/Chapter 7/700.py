class Item:

    def __init__(self, name, rate, quantity):
        self.name = name
        self.rate = rate
        self.quantity = quantity


class Bill:

    def __init__(self, customer_name, *items):
        self.customer_name = customer_name
        self.items = items
        self.itms = []