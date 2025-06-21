from . import constantes as c
from . import appointments_manager as schedule

def show_fields_info(info_list):
    for i, field in enumerate(info_list):
        print(f"{i+1}. {field}")

def hello(appointment_database, client_database, employee_database):

    options = c.HOME_OPTIONS

    while True:

        print("\n===== Hair Do =====")

        for i, name in enumerate(options):
            print(f"{i+1}. {name}")
        
        try:
            choice = int(input(f"Choose action (1 - {len(options)}): ")) - 1

        except ValueError:
            print(f"Invalid input. Please enter number (1 - {len(options)})")
            continue

        if 0 <= choice < len(c.HOME_OPTIONS):
            selected_option = options[choice]

            if selected_option == c.SCHEDULE:
                schedule.schedule()
            
            elif selected_option == c.MANAGE_CLIENTS:
                menu_contact_functions("client", c.CLIENT_FUNCTIONS, client_database)
            
            elif selected_option == c.MANAGE_EMPLOYEES:
                menu_contact_functions("employee", c.EMPLOYEE_FUNCTIONS, employee_database)
            
            elif selected_option == c.EXIT:
                exit_menu()
                return c.EXIT
        else:
            print(f"Invalid input. Please enter number (1 - {len(options)})")

def menu_contact_functions(contact_type, CONTACT_FUNCTIONS, contact_database):
    
    contact_function_list = list(CONTACT_FUNCTIONS.keys())
    
    print(f" ==== MANAGE {contact_type.upper()} DATABASE ====")

    for i, name in enumerate(contact_function_list):
        print(f"{i+1}. {name}")

    choice = int(input("Choose action: ")) - 1
    
    if 0 <= choice <= len(contact_function_list):
        selected_name = contact_function_list[choice]
        selected_function = CONTACT_FUNCTIONS[selected_name]
        return selected_function(contact_database)
    
    else:
        print("Invalid choice")
        return None

def exit_menu():
    print("Exiting program.")
    return "exit"