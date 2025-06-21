import random

from rich.table import Table
from rich.console import Console

from . import constantes as c
from . import app_interface as interface
from . import data_manager as data
from . import app_load as load

def add_contact(contact_type, FIELDS_INFO, JSON_FILE, contact_database):

    print()
    print(f"===== Adding new {contact_type} ====")
    print()

    contact = {}

    for field in FIELDS_INFO:
        if field == c.ID:
            value = generate_unique_id(contact_database)
        if field == c.PHONE:
            value = data.isvalid_phone()
        elif field == c.EMAIL:
            value = data.isvalid_email()
        elif field == c.BIRTH or field == c.HIRING:
            value = data.isvalid_date(field.lower())
        else:
            value = input(f"{contact_type.capitalize()} {field.lower()}").strip()
        
        contact[field] = value
    
    contact_database.append(contact)

    load.save_database(contact_type, JSON_FILE, contact_database)

    return contact_database

def modify_contact(contact_type, FIELDS_INFO, contact_database):
    """
    Modifies single contact in the contact database

    Args:
        contact_type (str) : Displayed contact type in user prompts
        FIELDS_INFO (list) : List of active fields for contact type (const)
        contact_database (list of dict): Contact database
    
    Returns:
        list of dict: Updated contact database
    """

    # Search contact for modification
    print(f"==== Search {contact_type} to modify ====")
    selected_contact_index = data.search_and_select_contact(contact_type, contact_database)

    # If no contact found, abort : 
    if selected_contact_index is None:
        return
    
    # Definition of contact
    contact = contact_database[selected_contact_index]

    # Modification of contact
    print(f"\n"
          f"==== Modify {contact_type} : {contact[c.LAST_NAME]}, {contact[c.FIRST_NAME]}===="
          "\n")
    
    # Show available fields for modification
    interface.show_fields_info(c.FIELDS_INFO)

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

        contact[field_chosen] = new_value

        print()
        print("\n"
              f"{contact_type} modified : {contact_database[selected_contact_index][c.LAST_NAME]}, {contact_database[selected_contact_index][c.FIRST_NAME]}")

        # Sort and save database
        load.save_database(contact_database)
    
    else:
        print("Invalid choice. Please enter valid number.")

def delete_contact(contact_type, contact_database):
    """
    Deletes single contact in the contact database

    Args:
        contact_type (str) : Displayed contact type in user prompts
        contact_database (list of dict): contact database

    Returns:
        list of dict: Updated contact database
    """


    # Search contact for deletion
    print(f"==== Search {contact_type} to delete ====")
    selected_contact_index = data.search_and_select_contact(contact_type, contact_database)
    
    # If no contact found, abort : 
    if selected_contact_index is None:
        return
    
    # User confirmation of contact deletion from contact database
    contact = contact_database[selected_contact_index]
    confirm = input("\n"
                    f"==== Delete {contact_type} : {contact[c.LAST_NAME]}, {contact[c.FIRST_NAME]} ? (y/n)\n"
                    "This operation can't be undone. Confirm?")
    
    if confirm != "y":
        print("Operation cancelled.\n")
        return

    # Delete contact from database
    contact_database.pop(selected_contact_index)
    print(f"\n"
          f"Deleted {contact_type} : {contact[c.LAST_NAME]}, {contact[c.FIRST_NAME]}"
          "\n")

    # Sort and save database
    load.save_database(contact_database)

    return contact_database

def show_all_contacts(contact_type, FIELD_INFO, contact_database):
    """Show contact list in a table.\n
    Only columns existing in at least one contact displayed 

    Args:
        contact_type (str) : Displayed contact type in user prompts
        FIELD_INFO (str): List of active fields for contact type (const)
        contact_database (list of dict): Contact database
    """

    console = Console()

    displayed_contacts_list = data.create_name_field(contact_database)
    
    # Create visible fields list from contact type (stored in a constant)
    visible_fields = ["Name"] + [
        field for field in FIELD_INFO
        if field not in (c.LAST_NAME, c.FIRST_NAME)
        and any(field in contact for contact in contact_database)
    ]

    # Create table
    table = Table(title=f"========== List of {contact_type} ==========")

    for field in visible_fields:
        table.add_column(field)

    # Add new line for each contact
    for contact in displayed_contacts_list:
        row = [contact.get(field, "—") for field in visible_fields]
        table.add_row(*row)

    # 4. Display table
    console.print(table)

def generate_unique_id(contact_database):
    """
    Generates a unique 4-digit ID not yet in contact_database.

    Args:
        contact_database (list of dict): Contact database

    Returns:
        str: Unique 4-digit ID
    """
    existing_ids = {contact.get(c.ID) for contact in contact_database if c.ID in contact}
    
    while True:
        new_id = f"{random.randint(0, 9999):04d}"  # Exemple: '0423'
        if new_id not in existing_ids:
            return new_id