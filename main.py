import hair_manager_app.app_load as load
import hair_manager_app.app_interface as interface

import hair_manager_app.constantes as c


#to do
def main():
    client_database = []
    employee_database = []
    appointments_database = []


    load.load_database("client", c.CLIENTS_JSON_FILE, client_database)
    load.load_database("employee", c.EMPLOYEES_JSON_FILE, employee_database)
    load.load_database("employee", c.APPOINTMENTS_JSON_FILE, appointments_database)
    while True:
        option = interface.hello(appointments_database, client_database, employee_database)
        if option == c.EXIT:
            break

    load.save_database("client", c.CLIENTS_JSON_FILE, client_database)
    load.save_database("employee", c.EMPLOYEES_JSON_FILE, employee_database)
    load.save_database("employee", c.APPOINTMENTS_JSON_FILE, appointments_database)

if __name__ == "__main__":
    main()