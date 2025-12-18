from employees import generate_employees
from customers import generate_customers
from items import generate_items
from transactions import generate_transactions

employees = generate_employees()
customers = generate_customers()
items = generate_items()

transactions = generate_transactions(customers, employees, items)

print("Employees:", len(employees))
print("Customers:", len(customers))
print("Items:", len(items))
print("Transactions:", len(transactions))
