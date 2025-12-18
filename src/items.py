import random

def generate_items(num_items: int = 200) -> dict:
    items = {}

    categories = ["tops", "pants", "shoes", "accessories"]

    for i in range(num_items):
        item_id = 500 + i
        items[item_id] = {
            "category": random.choice(categories),
            "price": round(random.uniform(10, 150), 2)
        }

    return items
