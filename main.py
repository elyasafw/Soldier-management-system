import soldier_manager as sm
import duty_manager as dm


def show_menu():
    print("--- Soldier duty management system ---\n")
    print("1. Add Soldier\n" \
        "2. Remove Soldier \n" \
        "3. View Soldiers\n" \
        "4. Add Duty\n" \
        "5. Update Status\n" \
        "6. View Duty \n" \
        "7. Exit\n")


def get_user_choice():
    valid_choice = False
    while not valid_choice:
        user_choice = input("Select an action from the menu (1-7):  ")
        if user_choice in "1234567":
            valid_choice = True
        print("Wrong choice.. Please choose only between 1-7")
    return user_choice


def handle_add_soldier():
    id = input("Enter new soldier ID:  ")
    name = input("Enter new soldier name:  ")
    sm.add_soldier(id, name)


def handle_remove_soldier():
    id = input("Enter soldier ID to remove:  ")
    sm.remove_soldier(id)


def handle_view_soldiers():
    sm.get_all_soldiers()


def handle_add_duty():
    pass


def handle_update_duty_status():
    pass


def handle_view_soldier_duties():
    pass


def main():
    pass