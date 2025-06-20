# Hair Manager

Application console pour gérer une base de clients, rendez-vous et employés d'un salon de coiffure.

## Installation

1. Clonez le dépôt depuis GitHub et entrez dans le dossier du projet.

2. (Optionnel) Créez et activez un environnement virtuel Python.  
   Sur Linux/macOS : `python -m venv venv` puis `source venv/bin/activate`  
   Sur Windows : `python -m venv venv` puis `venv\Scripts\activate`

3. Installez les dépendances avec :  
   `pip install -r requirements.txt`

## Utilisation

Pour lancer l'application, exécutez la commande suivante depuis la racine du projet :  
`python main.py`

## Tests

Pour lancer les tests unitaires avec pytest, utilisez la commande suivante depuis la racine du projet :  
`PYTHONPATH=. pytest tests/`

## Structure du projet

- `hair_manager_app/` : code source principal  
- `tests/` : tests unitaires  
- `data/` : fichiers JSON (clients, rendez-vous...)

## Contributions

Les contributions sont les bienvenues. Merci de faire une pull request.