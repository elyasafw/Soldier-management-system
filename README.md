# Soldier Duty Management System

A command-line system for managing soldier duty assignments in a military unit.

---

## Features

- Add and remove soldiers from the system
- Assign duties to soldiers (keeping, tour, kitchen, cleanliness, class attendant, logistics)
- Update duty status (pending / completed / missed)
- View all soldiers and their assigned duties
- Interactive submenus for quick follow-up actions
- Full input validation and error handling

---

## Project Structure

| File | Responsibility |
|------|---------------|
| `main.py` | Main menu, user input, routing |
| `soldier_manager.py` | Business logic for soldier management |
| `duty_manager.py` | Business logic for duty management |
| `until.py` | Helper and validation functions |
| `data.py` | Data storage (soldiers list, constants) |

---

## Data Structure

Each soldier is represented as a dictionary:

```python
{
    "id": 12345,
    "name": "David Cohen",
    "duties": [
        {
            "name": "keeping",
            "day": "sunday",
            "status": "pending"
        }
    ]
}
```

---

## System Rules

- Soldier ID must be unique
- Soldier name cannot be empty
- Duties can only be assigned on Sunday–Thursday (no Friday/Saturday)
- A soldier cannot have two duties with the same name
- Valid statuses: `pending`, `completed`, `missed`

---

## How to Run

```bash
python main.py
```

---

## Menu Options

```
1. Add Soldier
2. Remove Soldier
3. View Soldiers
4. Add Duty
5. Update Status
6. View Duty
7. Exit
```

---

## Example Usage

```
--- Soldier duty management system ---

Enter new soldier ID:  12345
Enter new soldier name:  David Cohen
Successfully added soldier (12345, David Cohen)

1. Add duty to this soldier
2. Back
Select an action: 1

Enter a soldier ID to add a duty:  12345
1. keeping
2. tour
3. kitchen
...
Select a duty from the list:  keeping
Enter day of week (Sunday - Thursday):  sunday
Duty added successfully
```
