class Coffee:
    all_coffees = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) == 0 or len(name) > 15:
            raise ValueError("Coffee name must be between 1 and 15 characters")
        self._name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) == 0 or len(value) > 15:
            raise ValueError("Coffee name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
