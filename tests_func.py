import hair_manager_app.data_manager as data
import hair_manager_app.app_load as load
import hair_manager_app.clients_manager as client
import hair_manager_app.appointments_manager as appointment

def main():
    client_database = []

    load.load_database(client_database)
    #appointment_database = {}
    #appointment.add_appointment(appointment_database, client_database)
    data.search_and_select_contact("client", client_database)

if __name__ == "__main__":
    main()