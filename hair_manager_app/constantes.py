import os
from . import clients_manager as clients
from . import app_interface as interface

# Contacts
TYPE = "Type"
CLIENT = "Client"
EMPLOYEE = "Employee"

# Informations
ID = "Contact ID"
FIRST_NAME = "First name"
LAST_NAME = "Last name"
ADDRESS = "Address"
PHONE = "Phone number"
EMAIL = "E-mail"
BIRTH = "Date of birth"
HIRING = "Date of hiring"

CLIENT_FIELDS_INFO = [LAST_NAME,
               FIRST_NAME,
               ADDRESS,
               PHONE,
               EMAIL,
               BIRTH,
               ID]

EMPLOYEE_FIELDS_INFO = [LAST_NAME,
               FIRST_NAME,
               ADDRESS,
               PHONE,
               EMAIL,
               BIRTH,
               HIRING,
               ID]

FIELDS_INFO = [LAST_NAME,
               FIRST_NAME,
               ADDRESS,
               PHONE,
               EMAIL,
               BIRTH,
               HIRING]


# Appointment
APP_DATE = "Date of appointment"
APP_START_HOUR = "Start hour"
APP_END_HOUR = "End hour"
APP_DURATION = "Duration"
SERVICE = "Service"
NOTES = "Notes"

# Regex

REGEX_DATE = r"^\d{4}[/-]\d{2}[/-]\d{2}$"
REGEX_DATE_STR = "yyyy/mm/dd"
REGEX_TIME = r"^\d{2}:\d{2}$"
REGEX_TIME_STR = "hh:mm"
REGEX_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
REGEX_EMAIL_STR = "xxx@xxx.xx"
REGEX_PHONE = r"^\d{3}[-\s]\d{4}$"
REGEX_PHONE_STR = "###-####"

# App functions

EXIT = "Exit"

# Clients
ADD_CLIENT = "Add new client"
MODIFY_CLIENT = "Modify client"
DELETE_CLIENT = "Delete client"
SHOW_ALL_CLIENTS = "Show all clients"

CLIENT_FUNCTIONS = {ADD_CLIENT: lambda db: clients.add_client(db),
                    MODIFY_CLIENT: lambda db: clients.modify_client(db),
                    DELETE_CLIENT: lambda db: clients.delete_client(db),
                    SHOW_ALL_CLIENTS: lambda db: clients.show_all_clients(db),
                    EXIT: lambda db: interface.exit_menu()
                    }
CLIENT_FUNCTION_LIST = list(CLIENT_FUNCTIONS.keys())

# Appointments
ADD_NEW_APPOINTMENT = "Add new appointment"
MODIFY_APPOINTMENT = "Modify an appointment"
DELETE_APPOINTMENT = "Delete an appointment"

# File management
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLIENTS_JSON_FILE = os.path.join(DATA_DIR, "clients.json")
APP_DIR = os.path.join(BASE_DIR, "hair_manager")

# Data (JSON)
APPOINTMENTS_JSON = os.path.join(DATA_DIR, "appointments.json")
CONTACTS_JSON = os.path.join(DATA_DIR, "clients.json")