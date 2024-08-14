# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:

# orders = [
#     ("Alice", "Laptop", 1),
#     ("Bob", "Camera", 2),
#     # More orders...
# ]
# - Write a function to iterate over the list of orders. 
# - Unpack each tuple in the list and format the details for display.

orders = [
("Alice", "Laptop", 1),
("Bob", "Camera", 2),
("John", "Gun", 3)
]

def placed_orders(orders):
    for order in orders: # here I start a loop that iterates over each tuple in the orders list
        customer_name, product, quantity = order # here is how I'm unpacking the tuple in my list
        print(f"{customer_name} ordered {quantity} {product}")

placed_orders(orders)