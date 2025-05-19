class Customer:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must be a string")
        if len(name) == 0 or len(name) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if len(value) == 0 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = value

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
         
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def most_aficionado(cls, coffee):
        max_price = 0
        top_customer = None
        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > max_price:
                max_price = total
                top_customer = customer
        return top_customer
