from data import Soldiers

def find_soldier_by_id(soldier_id: int):
    for soldier in Soldiers:
        for id in soldier.values():
            if id == soldier_id:
                return soldier
        return None


def find_duty_by_name(duties: list, duty_name: str):
    pass


def is_valid_name(name: str):
    if name.strip():
        return True
    return False


def is_valid_status(status: str):
    pass


def is_valid_day(day: str):
    pass