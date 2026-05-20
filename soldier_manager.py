from until import find_soldier_by_id, is_valid_name
from data import Soldiers


def add_soldier(soldier_id: int, name: str):
        if find_soldier_by_id(soldier_id):
             raise ValueError(f"ID number: {soldier_id} already exists in the system!")
        elif is_valid_name(name):
            raise ValueError(f"Invalid soldier name...")
        else:
            Soldiers.append({"id": soldier_id, "name": name, "duties": []})
            print("Successfully added soldier")


def remove_soldier(soldier_id: int):
    pass


def get_all_soldiers():
    pass