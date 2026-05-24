from data import soldiers, DAYS, STATUES


def find_soldier_by_id(soldier_id: int):
    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            return soldier
    return None


def find_duty_by_name(duties: list, duty_name: str):
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None


def is_valid_name(name: str):
    if name.strip():
        return True
    return False


def is_valid_status(status: str):
    return status in STATUES


def is_valid_day(day: str):
    return day in DAYS