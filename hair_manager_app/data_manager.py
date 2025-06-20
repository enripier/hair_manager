import re
import datetime
from . import constantes as c

# On crée une nouvelle liste de clients modifiés pour l'affichage

def create_name_field(database):
    """

    Create a "Name" field from first & last name :
    Name = "Last name, First name"

    """

    displayed_people_list = []

    # ==== OK ==== print(database)

    for person in database:

        # On crée un nouveau dictionnaire avec "Name" en premier
        displayed_person = {
            "Name": f"{person.get('Last name', '')}, {person.get('First name', '')}"
                             }
        # On ajoute tous les autres champs, sauf "Last name" et "First name"
        for key, value in person.items():

            if key not in ("Last name", "First name"):
                displayed_person[key] = value
        displayed_people_list.append(displayed_person)

    return displayed_people_list

def isvalid_email():
    """Check if email format is valid

    Returns:
        value | None : Valid value, or None if invalid
    """

    return isvalid_input("email", c.REGEX_EMAIL)

def isvalid_phone():
    """Check if phone format is valid

    Returns:
        value | None : Valid value, or None if invalid
    """
    return isvalid_input("phone number (###-####)", c.REGEX_PHONE)

def isvalid_input(prompt, regex):
    """Check if input format is valid

    Args:
        prompt (str): Name of input (displayed in user inputs)
        regex (str): Regex pattern to apply to the value.

    Returns:
        value | None : Valid value, or None if invalid
    """

    value = input(f"Enter {prompt}: ").strip()
    if not value:
        value = retry_empty_value(prompt)
        if value is None:
            return None
    while True:
        if re.match(regex, value):
            return value
        value = retry_isvalid(prompt)
        if value is None:
            return None
        
def retry_empty_value(prompt):
    while True:
        retry = input(f"No {prompt} entered. Retry? (y/n): ").strip().lower()
        match retry:
            case "y":
                return input(f"Enter {prompt}: ").strip()
            case "n":
                return None
            case _:
                print("Invalid choice. Enter 'y' or 'n'")

def retry_isvalid(fieldname):
    while True:
        retry = input(f"Invalid {fieldname}. Retry? (y/n): ").strip().lower()
        match retry:
            case "y":
                return input(f"Enter {fieldname}: ").strip()
            case "n":
                return None
            case _:
                print("Invalid choice. Enter 'y' or 'n'")

def isvalid_date(date_type):
    label = f"{date_type} date"
    date = input(f"Enter {date_type} (yyyy-mm-dd): ").strip()
    if not date:
        date = retry_empty_value(label)
        if date is None:
            return None
    while True:
        if re.match(c.REGEX_DATE, date):
            try:
                return datetime.datetime.strptime(date.replace("/", "-"), "%Y-%m-%d").date()
            except ValueError:
                pass
        date = retry_isvalid(date_type)
        if date is None:
            return None
        
def isvalid_time(label_time):
    """
    Demande une heure hh:mm, valide le format et la valeur.
    Renvoie un objet datetime.time ou None si abandon.
    """
    time = input(f"Enter {label_time} time (hh:mm): ").strip()

    if not time:
        time = retry_empty_value(label_time)
        if time is None:
            return None

    while True:
        if re.match(c.REGEX_TIME, time):
            hours = int(time[:2])
            minutes = int(time[3:])
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return datetime.time(hour= hours, minute= minutes)
        time = retry_isvalid(label_time)
        if time is None:
            return None
        
def search_contact(contact_type, contact_database):
    
    searched_contact = input(f"Search {contact_type}: ").lower()
    results = []
    for (i, contact) in enumerate(contact_database):
        # On regarde chaque champ du client
        for field in contact.values():
            if searched_contact in str(field).lower():
                results.append((i))
                break
    if not results:
        print("No such client found")
    else:
        return results

def search_and_select_contact(contact_type, contact_database):
    # Docstring OK
    """
        Search contact in contact database.

        Args:
            contact_type (str): Displayed contact type ("client", "employee"...)
            contact_database (list): Selected contact database (client, employee...)

        Returns:
            int | None: Contact index from contact_database, or None if cancelled.
        """

    # User input : searched contact
    searched_contact = input(f"Search {contact_type}: ").lower()

    # If no search term entered, abort operation
    if not searched_contact:
        searched_contact = ("Empty searched term. Operation cancelled.")
        return None

    # Create list of contact index & contact dict from search input
    found_contacts = [
        (contact_index, contact)
        for contact_index, contact in enumerate(contact_database)
        if any(searched_contact in str(value).lower() for value in contact.values())
    ]

    # If only one contact found, confirm and return said contact or abort operation
    if len(found_contacts) == 1:
        index, contact = found_contacts[0]
        confirm = input(f"Contact found : {contact['Last name']}, {contact['First name']} ? (y/n)")

        match confirm:
            case "y":
                return index
            case "n":
                print("\nOperation cancelled.\n")
            case _:
                print("\nInvalid input. Abort operation.\n")
        return None

    
    # If multiple contacts found -> create a list numbered from 1 and display it
    display_contacts_found = [
        (i+1, index, contact)
        for i, (index, contact) in enumerate(found_contacts)
    ]

    print(f"\n{contact_type}s found:")
    for i, index, contact in display_contacts_found:
        print(f"{i}. {contact.get(c.LAST_NAME)}, {contact.get(c.FIRST_NAME)}")
    
    # Ask user to choose one of them
    while True:
        choice = input("Choose contact number (blank to cancel): ").strip()

        if not choice:
            print("Selection cancelled.")
            return None  # CHANGEMENT : retour explicite sur annulation
        
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        selected_contact = int(choice)
        
        for i, index, contact in display_contacts_found:
            if i == selected_contact:
                return index  # CHANGEMENT : retour de l’index réel dans la base
        print("Invalid selection. Try again.")
    
def sort_contact_database(database):
    database.sort(key=lambda contact: (contact['Last name'], contact['First name']))
    return