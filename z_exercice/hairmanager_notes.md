# HAIR MANAGER :

@@@ À faire
+++ À vérifier
!!! Apprentissage en cours, à consolider

##  data

###     appointments.json

###     clients.json

###     employees.json

##  hair_manager_app

###     \__init.py\__

###     app_interface.py

                +++ À vérifier

###     app_load.py

                +++ À vérifier


####        def load_database(client_database)
                @@@ Adapter cette fonction pour toutes les databases et pas seulement clients

####        def save_database(client_database)
                +++ À vérifier

###     appointments_manager.py

###     @@@ À créer : contact_manager
                @@@ Faire des fonctions types pour les contacts
                @@@ Les adapter depuis clients_manager

###     clients_manager.py

####        def add_client(client_database)

                === Fonction OK ===
                === Docstring OK ===

####        def modify_client(client_database)

                === Fonction OK ===
                === Docstring OK ===

####        def delete_client(client_database)

                === Fonction OK ===
                === Docstring OK ===

####        def show_all_clients(client_database)

                === Fonction OK ===
                === Docstring OK ===

###     constantes.py

###     data_manager.py
####        def create_name_field(database):

                +++ À vérifier

####        def isvalid_email():

                +++ À vérifier

####        def isvalid_phone():

                +++ À vérifier

####        def isvalid_input(prompt, regex):

                +++ À vérifier

####        def retry_empty_value(prompt):

                +++ À vérifier

####        def retry_isvalid(fieldname):

                +++ À vérifier

####        def isvalid_date(date_type):

                +++ À vérifier

####        def isvalid_time(label_time):

                +++ À vérifier

####        def search_contact(contact_type, contact_database):

                @@@ Utile ?
                @@@ Peut-être search_and_select_contact suffit ?

####        def search_and_select_contact(contact_type, contact_database):

                +++ À vérifier

####        def sort_contact_database(database):

                +++ À vérifier

##  tests

##  launch.json

##  main.py