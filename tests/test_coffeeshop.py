import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        
        Customer.all_customers.clear()
        Coffee.all_coffees.clear()
        Order.all_orders.clear()

        self.customer1 = Customer("Tush")
        self.customer2 = Customer("Prudence")
        self.coffee1 = Coffee("Espresso")
        self.coffee2 = Coffee("Cappuccino")

        self.customer1.create_order(self.coffee1, 200)
        self.customer1.create_order(self.coffee2, 300)
        self.customer2.create_order(self.coffee1, 400)

    def test_customer_orders(self):
        orders = self.customer1.orders()
        self.assertEqual(len(orders), 2)
        self.assertTrue(all(order.customer == self.customer1 for order in orders))

    def test_customer_coffees(self):
        coffees = self.customer1.coffees()
        self.assertIn(self.coffee1, coffees)
        self.assertIn(self.coffee2, coffees)
        self.assertEqual(len(coffees), 2)

    def test_coffee_orders(self):
        orders = self.coffee1.orders()
        self.assertEqual(len(orders), 2)

    def test_coffee_customers(self):
        customers = self.coffee1.customers()
        self.assertIn(self.customer1, customers)
        self.assertIn(self.customer2, customers)
        self.assertEqual(len(customers), 2)

    def test_customer_name_validation(self):
     with self.assertRaises(TypeError):
        Customer(123) 
     with self.assertRaises(ValueError):
        Customer("") 
     with self.assertRaises(ValueError):
        Customer("a"*16) 
     c = Customer("ValidName")
     self.assertEqual(c.name, "ValidName")
     with self.assertRaises(TypeError):
        c.name = 456  
     with self.assertRaises(ValueError):
        c.name = "" 


    def test_coffee_num_orders(self):
        self.assertEqual(self.coffee1.num_orders(), 2)

    def test_coffee_average_price(self):
        self.assertEqual(self.coffee1.average_price(), (200 + 400) / 2)

    def test_most_aficionado(self):
        self.assertEqual(Customer.most_aficionado(self.coffee1), self.customer2)

if __name__ == '__main__':
    unittest.main()
