from . import constantes as c
from . import app_interface as interface
from . import data_manager as data
from . import app_load as load

def modify_client(client_database):
    print("==== Search client to modify ====")

    #Search client
    client_to_modify = data.search_and_select_contact("client", client_database)

    # If no client found, exit function
    if not client_to_modify:
        print("No such client found")
        return
    
    # Entering modification form
    print()
    print(f"==== Modify client : {client_database[client_to_modify]['Last name']}, {client_database[client_to_modify]['First name']} ====")
    print()
    interface.show_field_info(c.CLIENT_FIELDS_INFO)
    #for i, field in enumerate(c.FIELDS_INFO):
    #    print(f"{i+1}. {field}")
    print()

    # User choose which field they want to modify
    choice = input("Choose field to modify: ")
    choice = int(choice)
    choice -= 1
    
    if 0 <= choice <= len(c.FIELDS_INFO):
        field_chosen = c.FIELDS_INFO[choice]
        print(f"Modification of {field_chosen.lower()}")
        
        if field_chosen == c.PHONE:
            new_value = data.isvalid_phone()
        elif field_chosen == c.EMAIL:
            new_value = data.isvalid_email()
        elif field_chosen == c.BIRTH or field_chosen == c.HIRING:
            new_value = data.isvalid_date(field_chosen.lower())
        else:
            new_value = input(f"Enter new {field_chosen.lower()}: ")
        client_database[client_to_modify][c.FIELDS_INFO[choice]] = new_value
        print()
        print(f"Client modified : {client_database[client_to_modify][c.LAST_NAME]}, {client_database[client_to_modify][c.FIRST_NAME]}")

        load.save_database(client_database)
    
    else:
        print("Invalid choice. Please enter valid number.")
    