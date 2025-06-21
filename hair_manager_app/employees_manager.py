from rich.table import Table
from rich.console import Console

from . import constantes as c
from . import contacts_manager as contacts
from . import data_manager as data
from . import app_load as load

def add_employee(employee_database):
    #TODO
    return

def modify_employee(employee_database):
    """_summary_Modifies single employee in the employee database

    Args:
        employee_database (list of dict): employee database
    """

    contacts.modify_contact("employee", c.employee_FIELDS_INFO, employee_database)

def delete_employee(employee_database):
    """_summary_Deletes single employee in the employee database

    Args:
        employee_database (list of dict): employee database
    """

    contacts.delete_contact("employee", employee_database)

def show_all_employees(employee_database):
    """_summary_Show employee list in a table.\n
    Only columns existing in at least one employee displayed

    Args:
        employee_database (list of dict): employee database
    """
    contacts.show_all_contacts("employee", c.EMPLOYEE_FIELDS_INFO, employee_database)