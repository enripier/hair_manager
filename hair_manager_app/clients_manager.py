from . import constantes as c
from . import app_interface as interface
from . import data_manager as data
from . import app_load as load

from rich.table import Table
from rich.console import Console

def add_client(client_database):
    """
    Add new client to client database

    Args:
        client_database (list of dict): List of clients.

    Returns:
        list of dict: Updated client database with newly added client.
    """
    print()
    print("===== Adding new client ====")
    print()

    #User input : client informations
    client_first_name = input ("Client first name: ").strip()
    client_last_name = input ("Client last name: ").strip()
    client_address = input("Client address: ").strip()
    client_phone = data.isvalid_phone()
    client_email = data.isvalid_email()
    client_birth = data.isvalid_date("birth")

    #Client creation in a dict
    client = {
        c.FIRST_NAME: client_first_name,
        c.LAST_NAME: client_last_name,
        c.ADDRESS: client_address,
        c.PHONE: client_phone,
        c.EMAIL: client_email,
        c.BIRTH: client_birth
              }
    
    # Adding client to client database
    client_database.append(client)

    # Sorting & saving client database in JSON
    load.save_database(client_database)

    return client_database

def modify_client(client_database):
    """
    Modifies single client in the client database

    Args:
        client_database (list of dict): Client database
    
    Returns:
        list of dict: Updated client database
    """

    # Search client for modification
    print("==== Search client to modify ====")
    modified_client_index = data.search_and_select_contact("client", client_database)

    # If no client found, abort : 
    if modified_client_index is None:
        return
    
    # Definition of client
    client = client_database[modified_client_index]

    # Modification of client
    print(f"\n"
          f"==== Modify client : {client[c.LAST_NAME]}, {client[c.FIRST_NAME]}===="
          "\n")
    
    # Show available fields for modification
    interface.show_field_info(c.CLIENT_FIELDS_INFO)

    choice = input("\n"
                   "Choose field to modify: ").strip()

    if not choice.isdigit():
        choice = data.retry_isvalid("number")
        if choice is None:
            return
        
    choice = int(choice) -1
    
    # User chooses field to modify and enters new value
    if 0 <= choice < len(c.FIELDS_INFO):
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

        client[field_chosen] = new_value

        print()
        print("\n"
              f"Client modified : {client_database[modified_client_index][c.LAST_NAME]}, {client_database[modified_client_index][c.FIRST_NAME]}")

        # Sort and save database
        load.save_database(client_database)
    
    else:
        print("Invalid choice. Please enter valid number.")

def delete_client(client_database):
    """
    Deletes single client in the client database

    Args:
        client_database (list of dict): Client database

    Returns:
        list of dict: Updated client database
    """


    # Search client for deletion
    print("==== Search client to delete ====")
    selected_client_index = data.search_and_select_contact("client", client_database)
    
    # If no client found, abort : 
    if selected_client_index is None:
        return
    
    # User confirmation of client deletion from client database
    client = client_database[selected_client_index]
    confirm = input("\n"
                    f"==== Delete client : {client[c.LAST_NAME]}, {client[c.FIRST_NAME]} ? (y/n)\n"
                    "This operation can't be undone. Confirm?")
    
    if confirm != "y":
        print("Operation cancelled.\n")
        return

    # Delete client from database
    client_database.pop(selected_client_index)
    print()
    print(f"\n"
          f"Deleted client : {client[c.LAST_NAME]}, {client[c.FIRST_NAME]}"
          "\n")

    # Sort and save database
    load.save_database(client_database)

    return client_database

def show_all_clients(client_database):
    """Show client list in a table.\n
    Only columns existing in at least one user displayed 

    Args:
        client_database list of dict: Client database
    """

    console = Console()

    displayed_clients_list = data.create_name_field(client_database)
    
    # Créer la liste des champs visibles dynamiquement à partir des champs définis
    visible_fields = ["Name"] + [
        field for field in c.CLIENT_FIELDS_INFO
        if field not in ("Last name", "First name")
        and any(field in client for client in client_database)
    ]

    # Création du tableau
    table = Table(title="========== List of clients ==========")

    for field in visible_fields:
        table.add_column(field)

    print
    # Ajout des clients dans chaque ligne
    for client in displayed_clients_list:
        row = [client.get(field, "—") for field in visible_fields]
        table.add_row(*row)

    # 4. Affichage
    console.print(table)