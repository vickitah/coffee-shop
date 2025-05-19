## coffee shop challenge
This is a coffee shop system with Customers, Coffees, and Orders. This project demonstrates class relationships, instance tracking, and basic data validations.

## Features
1 .Create customers and coffees.

2 .Place orders linking customers and coffees with prices.

3 .Query orders by customer or coffee.

4 .Calculate statistics like number of orders and average price.

5 .Identify the customer who orders a particular coffee the most.

## setup
1. clone the repo
2. run python3 -m venv venv to create a virtual environment
3. install pip install pytest for running the tests
4. run pytest to run 

## How it works
1. Customer: Represents a customer with a name. Can create orders and retrieve their orders and coffees.

2. Coffee: Represents a type of coffee. Can retrieve all orders and customers for that coffee.

3. Order: Links a customer to a coffee with a price.

