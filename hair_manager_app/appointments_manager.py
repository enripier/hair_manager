from . import constantes as c
from . import data_manager as data



def schedule():
    print("\nNot implemented yet.\n")

#en cours
def add_appointment(appointment_database, client_database):
    
    # Client à chercher dans la database
    client = data.search_and_select_contact("client", client_database)
    print(client)

    # Type

    # Date + vérif format
    appointment_date = data.isvalid_date("appointment")

    # Enter heure début
    appointment_start_time = data.isvalid_time("appointment start")

    # Enter durée
    appointment_end_time = data.isvalid_time("appointment end")
    # Note

    appointment = {c.CLIENT: client_database[client], c.APPOINTMENT_DATE: appointment_date, c.START_HOUR: appointment_start_time, c.END_HOUR: appointment_end_time}

    print(appointment)
    return appointment

#to do
def modify_appointment():
    return

#to do
def delete_appointment():
    return

#to do
def show_appointments():
    return