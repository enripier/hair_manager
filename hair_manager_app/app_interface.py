from . import constantes as c

def show_field_info(info_list):
    for i, field in enumerate(info_list):
        print(f"{i+1}. {field}")

def menu_client_functions(client_database):
    
    print(" ==== MANAGE CLIENT DATABASE ====")
    
    #show_field_info(c.CLIENT_FIELDS_INFO)

    for i, name in enumerate(c.CLIENT_FUNCTION_LIST):
        print(f"{i+1}. {name}")
    
    choice = int(input("Choose action: ")) - 1
    
    if 0 <= choice <= len(c.CLIENT_FUNCTION_LIST):
        selected_name = c.CLIENT_FUNCTION_LIST[choice]
        selected_function = c.CLIENT_FUNCTIONS[selected_name]
        return selected_function(client_database)
    
    else:
        print("Invalid choice")
        return None

def exit_menu():
    print("Exiting program.")
    return "exit"