import json

from . import data_manager as data



def load_database(contact_type, json_file, contact_database):
    """
    Loads the contact database from JSON file.

    Args:
        contact_type (str) : Displayed contact type in user prompts
        json_file(str): JSON data file path
        contact_database (list of dict): List of contacts.

    Returns:
        list of dict: The created contact database with the JSON data.

    Raises:
        ###
    """
    try:
        with open(json_file, "r", encoding = "utf-8") as imported_file:
            json_data = json.load(imported_file)
            contact_database.extend(json_data)
            data.sort_contact_database(contact_database)
            print(f" ==== {contact_type} database loaded... ====")
            print()
            return contact_database
    
    except FileNotFoundError:
        print(f"File {json_file} doesn't exist. No contact database loaded.")
        return []
    
    except json.JSONDecodeError:
        print(f"Error reading JSON : {json_file} is corrupt or empty.")
        return []
    
    except OSError as e:
        print(f"Error opening {json_file} : {e}")
        return []

def save_database(contact_type, json_file, contact_database):
    """
    Saves the contact database to JSON file.

    Args:
        contact_type (str) : Displayed contact type in user prompts
        json_file(str): JSON data file path
        contact_database (list of dict): List of contacts.

    Returns:
        list of dict: The created contact database with the JSON data.

    Raises:
        ###
    """

    data.sort_contact_database(contact_database)

    try:
        with open(json_file, "w", encoding="utf-8") as exported_file:
            json.dump(contact_database, exported_file, indent = 4)
            print(f"{contact_type.capitalize()} database successfully saved")
    
    except OSError as e:
        print(f"Error saving {json_file} : {e}")