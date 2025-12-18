import random
from datetime import datetime, timedelta

def generate_transactions(
    customers: dict,
    employees: dict,
    items: dict,
    num_transactions: int = 5000
) -> list:

    transactions = []

    start_date = datetime(2024, 1, 1)

    for i in range(num_transactions):
        transaction = {
            "transaction_id": i + 1,
            "customer_id": random.choice(list(customers.keys())),
            "employee_id": random.choice(list(employees.keys())),
            "item_id": random.choice(list(items.keys())),
            "quantity": random.randint(1, 5),
            "date": start_date + timedelta(days=random.randint(0, 180))
        }
        transactions.append(transaction)

    return transactions
