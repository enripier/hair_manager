Je suis kéblo:

1. J'ai ça dans mes constantes :

# App functions

SCHEDULE = "Schedule"
MANAGE_CLIENTS = "Manage client database"
MANAGE_EMPLOYEES = "Manage employees database"
EXIT_APP = "Exit"


HOME = {SCHEDULE: "schedule",
        MANAGE_CLIENTS: lambda: interface.menu_contact_functions,
        MANAGE_EMPLOYEES: lambda: interface.menu_contact_functions,
        EXIT_APP: lambda: interface.exit_menu
        }
EXIT = "Exit"

2. J'ai ça dans mon app interface :

def hello():
    """
    print("Hello!\n"
    "What do you need?\n"
    "1. Manage schedule\n"
    "2. Manage clients\n"
    "3. Manage employees\n"
    "4. Exit")

    while True:
        choice = input("\n Choose menu number: ")
        
        match choice:
            case "1":
                result = menu_contact_functions("client", c.CLIENT_FUNCTIONS, client_database)
            case "4":
                return c.EXIT
"""

    for i, name in enumerate(c.HOME):
        print(f"{i+1}. {name}")
    
    choice = int(input(f"Choose action (1 - {len(c.HOME)}): ")) - 1

    if 0 <= choice < len(c.HOME):

3. Je veux appeler
schedule() qui n'existe pas encore pour SCHEDULE
interface.menu_contact_functions("client", c.CLIENT_FUNCTIONS, client_database) pour MANAGE_CLIENTS
interface.menu_contact_functions("employee", c.EMPLOYEE_FUNCTIONS, employee_database) pour MANAGE_EMPLOYEES
se barrer de l'app pour EXIT_APP

4. Je ne trouve pas la soluce