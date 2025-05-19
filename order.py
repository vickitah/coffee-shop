class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise TypeError("Order customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Order coffee must be a Coffee instance")
        if not (isinstance(price, int) or isinstance(price, float)):
            raise TypeError("Order price must be a number")
        if price <= 0:
            raise ValueError("Order price must be positive")
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
