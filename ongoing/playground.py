from rich.table import Table
from rich.console import Console

import hair_manager_app.constantes as c
import hair_manager_app.clients_manager as clients
import hair_manager_app.data_manager as data
import hair_manager_app.app_load as load



def add_contact(contact_type, FIELDS_INFO, JSON_FILE, contact_database):

    print()
    print(f"===== Adding new {contact_type} ====")
    print()

    contact = {}

    for field in FIELDS_INFO:
        if field == c.ID:
            continue
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








    return


    #User input : contact informations
    contact_first_name = input ("contact first name: ").strip()
    contact_last_name = input ("contact last name: ").strip()
    contact_address = input("contact address: ").strip()
    contact_phone = data.isvalid_phone()
    contact_email = data.isvalid_email()
    contact_birth = data.isvalid_date("birth")

    #contact creation in a dict
    contact = {
        c.FIRST_NAME: contact_first_name,
        c.LAST_NAME: contact_last_name,
        c.ADDRESS: contact_address,
        c.PHONE: contact_phone,
        c.EMAIL: contact_email,
        c.BIRTH: contact_birth
              }
    
    # Adding contact to contact database
    contact_database.append(contact)

    # Sorting & saving contact database in JSON
    load.save_database("contact", c.contactS_JSON_FILE, contact_database)

    return contact_database