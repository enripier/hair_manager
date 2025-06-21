from rich.table import Table
from rich.console import Console

from . import constantes as c
from . import contacts_manager as contacts
from . import data_manager as data
from . import app_load as load



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
    load.save_database("client", c.CLIENTS_JSON_FILE, client_database)

    return client_database

def modify_client(client_database):
    """_summary_Modifies single client in the client database

    Args:
        client_database (list of dict): Client database
    """

    contacts.modify_contact("client", c.CLIENT_FIELDS_INFO, client_database)

def delete_client(client_database):
    """_summary_Deletes single client in the client database

    Args:
        client_database (list of dict): Client database
    """

    contacts.delete_contact("client", client_database)

def show_all_clients(client_database):
    """_summary_Show client list in a table.\n
    Only columns existing in at least one client displayed

    Args:
        client_database (list of dict): Client database
    """
    contacts.show_all_contacts("client", c.CLIENT_FIELDS_INFO, client_database)