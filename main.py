import soldier_manager as sm
import duty_manager as dm
import data as d


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
    while True:
        user_choice = input("Select an action from the menu (1-7):  ")
        if user_choice in "1234567":
            return user_choice
        print("Wrong choice.. Please choose only between 1-7")


def handle_add_soldier():
    try:
        id = int(input("Enter new soldier ID:  "))
        name = input("Enter new soldier name:  ")
        sm.add_soldier(id, name)
        while True:
            print("\n1. Add duty to this soldier\n2. Back")
            choice = input("Select an action: ")
            if choice == "1":
                handle_add_duty()
            elif choice == "2":
                break
            else:
                print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")


def handle_remove_soldier():
    try:
        id = int(input("Enter soldier ID to remove:  "))
        sm.remove_soldier(id)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def handle_view_soldiers():
    sm.get_all_soldiers()
    while True:
        print("\n1. Add soldier\n2. Remove soldier\n3. Add duty to soldier\n4. Back")
        choice = input("Select an action: ")
        if choice == "1":
            handle_add_soldier()
        elif choice == "2":
            handle_remove_soldier()
        elif choice == "3":
            handle_add_duty()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def handle_add_duty():
    try:
        id = int(input("Enter a soldier ID to add a duty:  "))
        for i, j in enumerate(d.DUTIES):
            print(f"{i+1}. {j}")
        while True:
            duty = input("Select a duty from the list:  ")
            if duty in d.DUTIES:
                break
            print("Invalid duty... Please select an existing duty only!")
        day = input("Enter day of week (Sunday - Thursday):  ")
        dm.add_duty(id, duty, day)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def handle_update_duty_status():
    try:
        id = int(input("Enter a soldier ID to update a duty status:  "))
        for i, j in enumerate(d.DUTIES):
            print(f"{i}: {j}")
        while True:
            duty = input("Select a duty from the list:  ")
            if duty in d.DUTIES:
                break
            print("Invalid duty... Please select an existing duty only!")
        status = input("Enter status for duty (pending / completed / missed):  ")
        dm.update_duty_status(id, duty, status)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def handle_view_soldier_duties():
    try:
        id = int(input("Enter Soldier ID to view duties:  "))
        dm.get_soldier_duties(id)
        while True:
            print("\n1. Add duty\n2. Update duty status\n3. Back")
            choice = input("Select an action: ")
            if choice == "1":
                handle_add_duty()
            elif choice == "2":
                handle_update_duty_status()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def main():
    actions = {
        "1": handle_add_soldier,
        "2": handle_remove_soldier,
        "3": handle_view_soldiers,
        "4": handle_add_duty,
        "5": handle_update_duty_status,
        "6": handle_view_soldier_duties,
    }
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == "7":
            print("Goodbye!")
            break
        actions[choice]()


if __name__ == "__main__":
    main()