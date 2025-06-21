import os

from . import clients_manager as clients
from . import employees_manager as employees
from . import app_interface as interface

# Contacts
CONTACT_TYPE = "Type"
CLIENT = "Client"
EMPLOYEE = "Employee"

FIRST_NAME = "First name"
LAST_NAME = "Last name"
ADDRESS = "Address"
PHONE = "Phone number"
EMAIL = "E-mail"
BIRTH = "Date of birth"
HIRING = "Date of hiring"

ID = "Contact ID"

# Services
SERVICE_LABEL = "Service"
DESCRIPTION = "Description"
DURATION = "Duration"

# Time & Durations
APPOINTMENT_DATE = "Date of appointment"
START_HOUR = "Start hour"
END_HOUR = "End hour"
DURATION = "Duration"

# Misc

NOTES = "Notes"

# Contact fields


CLIENT_FIELDS_INFO = [LAST_NAME,
               FIRST_NAME,
               ADDRESS,
               PHONE,
               EMAIL,
               BIRTH,
               CONTACT_TYPE,
               ID]

EMPLOYEE_FIELDS_INFO = [LAST_NAME,
               FIRST_NAME,
               ADDRESS,
               PHONE,
               EMAIL,
               BIRTH,
               HIRING,
               CONTACT_TYPE,
               ID]

APPOINTMENTS_FIELDS = [
    CLIENT,
    EMPLOYEE,
    APPOINTMENT_DATE,
    START_HOUR,
    END_HOUR,
    DURATION,
    SERVICE_LABEL,
    NOTES
]

SERVICE_FIELDS = [
    SERVICE_LABEL,
    DESCRIPTION,
    DURATION
]


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

SCHEDULE = "Schedule"
MANAGE_CLIENTS = "Manage client database"
MANAGE_EMPLOYEES = "Manage employee database"
EXIT = "Exit"


HOME_OPTIONS = [
    SCHEDULE,
    MANAGE_CLIENTS,
    MANAGE_EMPLOYEES,
    EXIT
    ]

# Contacts functions
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

ADD_EMPLOYEE = "Add new employee"
MODIFY_EMPLOYEE = "Modify employee"
DELETE_EMPLOYEE = "Delete employee"
SHOW_ALL_EMPLOYEES = "Show all employees"

EMPLOYEE_FUNCTIONS = {ADD_EMPLOYEE: lambda db: employees.add_employee(db),
                      MODIFY_EMPLOYEE: lambda db: employees.modify_employee(db),
                      DELETE_EMPLOYEE: lambda db: employees.delete_employee(db),
                      SHOW_ALL_EMPLOYEES: lambda db: employees.show_all_employees(db)
                      }

# Appointments
ADD_NEW_APPOINTMENT = "Add new appointment"
MODIFY_APPOINTMENT = "Modify an appointment"
DELETE_APPOINTMENT = "Delete an appointment"

# File management
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
APP_DIR = os.path.join(BASE_DIR, "hair_manager")

# Data (JSON)
CLIENTS_JSON_FILE = os.path.join(DATA_DIR, "clients.json")
EMPLOYEES_JSON_FILE = os.path.join(DATA_DIR, "employees.json")
APPOINTMENTS_JSON_FILE = os.path.join(DATA_DIR, "appointments.json")