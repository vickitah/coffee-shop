from customer import Customer
from coffee import Coffee
from order import Order



cust1 = Customer("Victor")
cust2 = Customer("Prudence")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

cust1.create_order(coffee1, 3.5)
cust1.create_order(coffee2, 5.0)
cust2.create_order(coffee1, 4.0)


print(cust1.orders())       
print(cust1.coffees())       
print(coffee1.customers())  
print(coffee1.num_orders()) 
print(coffee1.average_price()) 
