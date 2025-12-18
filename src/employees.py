import random

FIRST_NAMES = [
    "James", "Michael", "Robert", "John", "David",
    "Elif", "Tithi", "Adithya", "William", "Richard", "Bradley",
    "Mary", "Patricia", "Ali", "Elizabeth", "Jennifer", "Tiffany",
    "David", "Barbara", "Richard", "Susan", "Joseph",
    "Jessica", "Thomas", "Sarah", "Charles", "Karen"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown",
    "Jones", "Oz", "Johnson", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson",
    "Anderson", "Thomas", "Taylor", "Moore",
    "Jackson", "Martin"
]


def generate_employees(
    num_employees: int = 2000,
    starting_employee_id: int = 100,
    starting_store_id: int = 200
) -> dict:
    """
    Generate employee data for a retail store chain.
    """

    employee_store_dict = {}

    for i in range(num_employees):
        employee_id = starting_employee_id + i
        store_id = starting_store_id + i

        role = "manager" if i < 10 else "staff"

        employee_store_dict[employee_id] = {
            "store_id": store_id,
            "first_name": random.choice(FIRST_NAMES),
            "last_name": random.choice(LAST_NAMES),
            "age": random.randint(18, 75),
            "role": role
        }

    return employee_store_dict
