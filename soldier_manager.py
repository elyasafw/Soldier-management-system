from until import find_soldier_by_id, is_valid_name
from data import soldiers


def add_soldier(soldier_id: int, name: str):
        if find_soldier_by_id(soldier_id):
            raise ValueError(f"ID number: {soldier_id} already exists in the system!")
        elif is_valid_name(name):
            raise ValueError(f"Invalid soldier name...")
        else:
            soldiers.append({"id": soldier_id, "name": name, "duties": []})
            print(f"Successfully added soldier ({soldier_id, name})")


def remove_soldier(soldier_id: int):
    if not find_soldier_by_id(soldier_id):
            raise ValueError(f"ID number: {soldier_id} does not exist in the system!")
    else:
        for solider in soldiers:
            if solider["id"] == soldier_id:
                soldiers.remove(solider)
                print("Soldier removal was successful")
                break


def get_all_soldiers():
    pass