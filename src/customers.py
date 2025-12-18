import random

def generate_customers(num_customers: int = 3000) -> dict:
    customers = {}

    for i in range(num_customers):
        customer_id = 1000 + i
        customers[customer_id] = {
            "age": random.randint(18, 75),
            "gender": random.choice(["male", "female"]),
            "loyalty_member": random.choice([True, False])
        }

    return customers
