from . import constantes as c
from . import data_manager as data
import json
from pathlib import Path
import os

def load_database(client_database):
    #TODO : Adapter cette fonction pour toutes les databases et pas seulement clients
    """
    Load the client database from JSON file.

    Args:
        client_database (list of dict): List of clients.

    Returns:
        list of dict: The created client database with the JSON data.

    Raises:
        ###
    """
    json_file = c.CLIENTS_JSON_FILE
    try:
        if os.path.exists(json_file):
            with open(json_file, "r", encoding = "utf-8") as imported_file:
                json_data = json.load(imported_file)
                client_database.extend(json_data)
                data.sort_contact_database(client_database)
                print(" ==== Client database loaded... ====")
                print()
                return client_database
    
    except FileNotFoundError:
        print(f"File {json_file} n'existe pas. No client database loaded.")
        return []
    except json.JSONDecodeError:
        print(f"Erreur de lecture JSON : le fichier {json_file} est corrompu ou vide.")
        return []
    except OSError as e:
        print(f"Erreur lors de l'ouverture du fichier JSON : {e}")
        return []

def save_database(client_database):

    data.sort_contact_database(client_database)

    json_file = c.CLIENTS_JSON_FILE

    try:
        with open(json_file, "w") as exported_file:
            json.dump(client_database, exported_file, indent = 4)
            print = ("Client database successfully saved")
    
    except OSError as e:
        print(f"Erreur lors de l'enregistrement du fichier JSON : {e}")

client_database = []
appointments_database = []
employees_database = []
#print(client_database)
#load_database(client_database)