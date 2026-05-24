import until as u
from data import soldiers


def add_duty(soldier_id: int, duty_name: str, day: str):
    soldier = u.find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"ID number: {soldier_id} does not exist in the system!")
    if u.find_duty_by_name(soldier["duties"], duty_name):
        raise ValueError("The soldier already has a duty with the same name!")
    if not u.is_valid_day(day):
        raise ValueError("It is not possible to schedule a duty for this day...")
    soldier["duties"].append({"name": duty_name, "day": day, "status": "pending"})
    print("Duty added successfully")


def update_duty_status(soldier_id: int, duty_name: str, new_status: str):
    soldier = u.find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"ID number: {soldier_id} does not exist in the system!")
    duty = u.find_duty_by_name(soldier["duties"], duty_name)
    if not duty:
        raise KeyError("No duty was found for the requested soldier!")
    if not u.is_valid_status(new_status):
        raise ValueError("Invalid status!")
    print(f"Status updated successfully! ({duty['status']} -> {new_status})")
    duty["status"] = new_status
    

def get_soldier_duties(soldier_id: int):
    soldier = u.find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"ID number: {soldier_id} does not exist in the system!")
    duties_str = " | ".join(
        f"{d['name']}, {d['day']}, {d['status']}" for d in soldier["duties"]
    )
    print(f"  {duties_str}")