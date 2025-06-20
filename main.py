#import os
#import json

#from pathlib import Path
#from rich.table import Table
#from rich.console import Console
#from datetime import datetime

import hair_manager_app.data_manager as data
import hair_manager_app.app_load as load
import hair_manager_app.app_interface as interface
import hair_manager_app.clients_manager as clients
import hair_manager_app.constantes as c


#to do
def main():
    client_database = []
    #appointments_database = []
    #employees_database = []

    load.load_database(client_database)
    
    while True:
        result = interface.menu_client_functions(client_database)
        if result == "exit":
            break

    load.save_database(client_database)

if __name__ == "__main__":
    main()