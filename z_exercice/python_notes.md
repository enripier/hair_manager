# Python : Fonctions & méthodes

[TOC]

## A. Introduction / Généralités

### A.1. Noyau Python

#### A.1.1. Built-in : Fonctions classiques

##### `all()`

Retourne `True` si tous les éléments sont vrais (ou si vide).

##### `any()`

Retourne `True` si au moins un élément de l’itérable est vrai.

##### `enumerate()`

Permet d’itérer avec index + valeur sur une liste, tuple, etc.

Exemple : `for i, v in enumerate(...)` , i est l’index, v la valeur.

##### `isinstance()`

Description : Vérifie si un objet est d’un type donné.

**Syntaxe** : isinstance(objet, type)

**Exemple** : isinstance("test", str) renvoie True

##### `list()`

Convertit un objet itérable en liste.

##### `range()`

Crée une séquence de nombres (par défaut de 0 à n-1)

**Syntaxe** : range(stop), range(start, stop), range(start, stop, step)

**Exemple** : range(3) → 0, 1, 2

##### `type()`

Retourne le type d’un objet (str, int, list…)

#### A.1.2. Built-in : Fonctions anonymes

##### `lambda`

**Expression anonyme** qui permet de créer une fonction simple, courte, **sans nom**.

Utile pour définir rapidement une petite fonction « à la volée », notamment quand on a besoin de passer une fonction en argument (ex : fonctions de tri, filtres, callbacks).

**Syntaxe**

```python
lambda arguments: expression

# arguments : paramètres de la fonction (comme dans une fonction classique).
# expression : une seule expression qui est évaluée et retournée automatiquement (pas besoin de return).
```

**Exemple simple** :

```python
add = lambda x, y: x + y
print(add(3, 4))  # Affiche 7
```

**Exemple avec tri** :

```python
data = [(1, 'a'), (2, 'b'), (3, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])  # Trie par la deuxième valeur du tuple
```

**Points importants** :

- Fonction utile pour les petites fonctions rapides.
- Ne peut contenir qu’une seule expression, pas de bloc complexe.
- Pas de nom, donc ne s’utilise pas pour des fonctions complexes à plusieurs lignes.
- Très fréquente dans les dictionnaires de fonctions

**Erreurs courantes** :

- Essayer d’écrire plusieurs lignes dans une lambda (pas possible).
- Confondre lambda avec def (une fonction nommée classique).
- Mauvaise utilisation des arguments (oubli de : ou parenthèses).

## B. Gestion des erreurs

##### **`try`** / `except`

`try` démarre un bloc de code dont les erreurs peuvent être interceptées.
`except` capture et gère une erreur survenue dans le bloc try

**Syntaxe** : `try:` / `except ErreurType as e:`

**Exemple** :

```python
try:
    x = int(input("Nombre : "))
except ValueError:
    print("Ce n'est pas un nombre.")
```

##### `ValueError`

Erreur levée quand une valeur est du mauvais type (ex. : convertir "abc" en int).

**Exemple** : `int("abc")`  provoque une ValueError

##### `FileNotFoundError`

Erreur levée quand un fichier est introuvable.

**Exemple** : `open("fichier-inexistant.txt", "r")`  provoque une FileNotFoundError

## C. Types et leurs méthodes

#### C.1. Fonctions liées aux chaînes de caractères

##### `str.lower()`

Renvoie la chaîne avec toutes les lettres en minuscules.

**Exemple** : `"Bonjour".lower()` → "bonjour"

##### `str.upper()`

Renvoie la chaîne avec toutes les lettres en majuscules.

**Exemple** : `"salut".upper()` → `"SALUT"`

##### `str.strip()`

Supprime les espaces (ou caractères) au début et à la fin.

**Exemple** : `" texte ".strip()` → `"texte"`

##### `str.lstrip()`

Retourne une nouvelle chaîne où les **caractères de gauche** (début de la chaîne) spécifiés sont supprimés.
Si aucun caractère n’est passé en argument, enlève les espaces blancs (espaces, tabulations, retours à la ligne) en début.

**Exemple** :

```python
nouvelle_chaine = chaine.lstrip(chars) 			# chars (optionnel)`
```

##### `str.rstrip()`

Retourne une nouvelle chaîne où les **caractères de droite** (fin de la chaîne) spécifiés sont supprimés.
Si aucun caractère n’est passé en argument, enlève les espaces blancs en fin.

**Exemple** :

```python
nouvelle_chaine = chaine.rstrip(chars)			# chars (optionnel)
```

##### `str.split()`

Coupe la chaîne en une liste de morceaux selon un séparateur.

**Syntaxe** : `str.split(sep)` — si sep n’est pas précisé, coupe sur les espaces.

**Exemple** : `"a,b,c".split(",")` → `["a", "b", "c"]`

##### `str.join()`

Assemble une liste de chaînes en une seule, séparée par un séparateur.

**Syntaxe** : `"séparateur".join(liste)`

**Exemple** : `", ".join(["Alice", "Bob"])` → `"Alice, Bob"`

##### `str.isdigit()`

Retourne True si la chaîne ne contient que des chiffres.

**Exemple** : `"123".isdigit()` → `True`, `"12a".isdigit()` → `False`

##### `str.replace()`

Remplace une sous-chaîne par une autre.

**Syntaxe** : `str.replace(ancien, nouveau)`

**Exemple** : `"2025-06".replace("-", "/")` → `"2025/06"`

##### `str.startswith()`

Vérifie si la chaîne commence par un certain texte.

**Exemple** : `"agenda.json".startswith("a")` → `True`

#### C.2. Méthodes sur les listes.

##### `list.append()`

Ajoute un élément à la fin de la liste.

**Syntaxe** : `liste.append(element)`

**Exemple** :

```python
fruits = ["pomme", "banane"]
fruits.append("orange")
# fruits devient ["pomme", "banane", "orange"]
```

##### `list.pop()`

Supprime et retourne un élément de la liste. Par défaut, le dernier élément (si aucun index précisé).

Renvoie une erreur `IndexError` :

- si la liste est vide ( `pop from empty list` )

- si l’index est hors limites ( `pop index out of range` )

**Syntaxe** :

```python
liste.pop()        # dernier élément
liste.pop(index)   # élément à l’index donné
```

**Exemple :**

```python
ma_liste = [10, 20, 30, 40]

dernier = ma_liste.pop()       # enlève et retourne 40
print(dernier)                 # affiche : 40
print(ma_liste)                # affiche : [10, 20, 30]

element_1 = ma_liste.pop(1)    # enlève et retourne l’élément à l’index 1 (20)
print(element_1)               # affiche : 20
print(ma_liste)                # affiche : [10, 30]

# ma_liste.pop(10)  # provoquerait IndexError : pop index out of range
```

##### `list.remove()`

Supprime la première occurrence d’un élément dans la liste.

**Syntaxe** : `liste.remove(element)`

**Attention** : Provoque une erreur `ValueError` si l’élément n’existe pas.

**Exemple** :

```python
fruits = ["pomme", "banane", "orange"]
fruits.remove("banane")
# fruits devient ["pomme", "orange"]
```

##### `list.sort()`

Trie la liste sur place (modifie la liste).

**Syntaxe** : `liste.sort()`

**Exemple** :

```python
nombres = [5, 3, 9]
nombres.sort()
# nombres devient [3, 5, 9]
```

##### `list.index()`

Renvoie l’index de la première occurrence d’un élément.

**Syntaxe** : `liste.index(element)`

**Attention** : Provoque une erreur `ValueError` si l’élément n’existe pas.

**Exemple** :

```python
fruits = ["pomme", "banane"]
fruits.index("banane")  # renvoie 1
```

##### `list.insert()`

Insère un élément à une position donnée.

**Syntaxe** : `liste.insert(index, element)`

**Exemple** :

```python
fruits = ["pomme", "orange"]
fruits.insert(1, "banane")
# fruits devient ["pomme", "banane", "orange"]
```

#### C.3. Méthodes sur les dictionnaires (dict)

##### `dict.get()`

Retourne la valeur associée à une clé, ou une valeur par défaut si la clé n’existe pas.

**Syntaxe** : `dictionnaire.get(cle, valeur_par_defaut)`

**Exemple** :

```python
contact = {"nom": "Alice"}
contact.get("tel", "Non renseigné")  # renvoie "Non renseigné"
```

##### `dict.keys()`

Renvoie un objet contenant toutes les clés du dictionnaire.

**Syntaxe** : `dictionnaire.keys()`

**Exemple** :

```python
d = {"a": 1, "b": 2}
list(d.keys())  # renvoie ["a", "b"]
```

##### `dict[key]`

Accède à la valeur associée à une clé dans un dictionnaire.
Renvoie une erreur `KeyError` si la clé est absente

**Syntaxe :**`valeur = mon_dict[cle]`

**Exemple :**

```python
mon_dict = {"nom": "Alice", "age": 30}

print(mon_dict["nom"])      # affiche : Alice

# print(mon_dict["ville"]) # provoque KeyError car "ville" n’existe pas

# Solution sûre avec .get()
print(mon_dict.get("ville"))           # affiche : None (pas d’erreur)
print(mon_dict.get("ville", "Paris"))  # affiche : Paris (valeur par défaut)
```

##### `dict.get()`

Permet d’accéder à la valeur associée à une clé dans un dictionnaire **sans provoquer d’erreur** si la clé n’existe pas.
Retourne la valeur associée à la clé si elle existe, sinon, la valeur par défaut (ou `None` si non précisée)

**Syntaxe** : `valeur = mon_dict.get(cle, valeur_par_defaut)`

**Exemple** :

```python
mon_dict = {"fruit": "pomme", "quantite": 5}

print(mon_dict.get("fruit"))           # affiche : pomme
print(mon_dict.get("prix"))            # affiche : None (clé absente)
print(mon_dict.get("prix", 0))         # affiche : 0 (valeur par défaut)
```

##### `dict.values()`

Renvoie un objet contenant toutes les valeurs du dictionnaire.

**Syntaxe** : `dictionnaire.values()`

**Exemple** :

```python
d = {"a": 1, "b": 2}
list(d.values())  # renvoie [1, 2]
```

##### `dict.items()`

Renvoie un objet contenant les paires clé-valeur sous forme de tuples.

**Syntaxe** : `dictionnaire.items()`

**Exemple** :

```python
d = {"a": 1, "b": 2}
list(d.items())  # renvoie [("a", 1), ("b", 2)]
```

##### `dict.update()`

Met à jour un dictionnaire avec les clés et valeurs d’un autre dictionnaire.

**Syntaxe** : `dictionnaire.update(autre_dictionnaire)`

**Exemple** :

```python
d = {"a": 1}
d.update({"b": 2})
# d devient {"a": 1, "b": 2}
```

##### `dict.pop()`

Supprime une clé du dictionnaire et renvoie sa valeur.

**Syntaxe** : `dictionnaire.pop(cle)`

**Attention** : Provoque une erreur si la clé n’existe pas (sauf si valeur par défaut donnée).

**Exemple** :

```python
d = {"a": 1, "b": 2}
d.pop("a")  # renvoie 1, d devient {"b": 2}
```

## D. Modules standard importants

#### D.1. Module re (expressions régulières)

##### `.match()`

Vérifie si une chaîne commence **exactement** par un motif donné (regex).
Elle renvoie un objet “match” si ça correspond, sinon `None`.

re.match() ne vérifie qu’au **début de la chaîne**, il faut utiliser `search()` sinon.

**Syntaxe** :

```python
import re
re.match(motif, chaine)
```

**Exemple :**

```python
import re
texte = "2025-06-17 14:00"
if re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", texte):
    print("Format valide")
else:
    print("Format invalide")
```



##### `.search()`

Cherche un motif n’importe où dans la chaîne, pas seulement au début, contrairement à `re.match()` .
Elle renvoie un objet “match” si le motif est trouvé quelque part, `None` sinon

**Syntaxe :**

```python
import re
re.search(motif, chaine)
```

**Exemple :**

```python
import re
texte = "Rendez-vous le 17/06/2025 à 14:00"
if re.search(r"\d{2}/\d{2}/\d{4}", texte):
    print("Date trouvée !")
```

#### D.2. Module csv

##### `csv.reader()`

Lit un fichier CSV ligne par ligne et retourne un itérateur de listes (chaque liste représente une ligne).

**Utilisation** : Utile pour lire un fichier CSV simple.

**Exemple** :

```python
import csv
with open("contacts.csv", "r", newline="") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)  # liste de valeurs pour chaque ligne
```

##### `csv.writer()`

Permet d’écrire des lignes (listes) dans un fichier CSV.

**Utilisation** : Utile pour écrire des données dans un fichier CSV.

**Exemple** :

```python
import csv
with open("contacts.csv", "w", newline="") as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerow(["nom", "tel"])
    ecrivain.writerow(["Alice", "123456"])
```

##### `csv.DictReader()`

Lit un fichier CSV et retourne un itérateur de dictionnaires (avec clés basées sur la première ligne).

**Utilisation** : Pratique pour accéder aux données CSV par noms de colonnes.

**Exemple** :

```python
import csv
with open("contacts.csv", "r", newline="") as fichier:
    lecteur = csv.DictReader(fichier)
    for contact in lecteur:
        print(contact["nom"])
```

##### `csv.DictWriter()`

Permet d’écrire des dictionnaires dans un fichier CSV, en utilisant les clés comme noms de colonnes.

**Utilisation** : Utile pour écrire des données structurées avec noms de colonnes.

**Exemple** :

```python
import csv
with open("contacts.csv", "w", newline="") as fichier:
    champs = ["nom", "tel"]
    ecrivain = csv.DictWriter(fichier, fieldnames=champs)
    ecrivain.writeheader()
    ecrivain.writerow({"nom": "Alice", "tel": "123456"})
```

#### D.3. Module json

##### `json.load()`

Lit un fichier JSON et retourne l’objet Python correspondant (liste, dictionnaire, etc.).

**Exemple** :

```python
import json
with open("agenda.json", "r") as fichier:
    data = json.load(fichier)
```

##### `json.dump()`

Écrit un objet Python dans un fichier au format JSON.

**Syntaxe** : `json.dump(objet, fichier, indent=4)`

**Exemple** :

```python
import json
with open("agenda.json", "w") as fichier:
    json.dump(data, fichier, indent=4)
```

#### D.4. Module os

##### `os.path.exists()`

Vérifie si un fichier ou un dossier existe à un chemin donné.

**Syntaxe** : `os.path.exists(chemin)`

**Retour** : True si le chemin existe, sinon False.

**Exemple** :

```python
import os
if os.path.exists("contacts.csv"):
    print("Le fichier existe.")
```

##### `os.remove()`

Supprime un fichier.

**Syntaxe** : `os.remove(chemin_fichier)`

**Attention** : Provoque une erreur si le fichier n’existe pas.

**Exemple** :

```python
import os
os.remove("contacts.csv")
```

##### `os.mkdir()`

Crée un nouveau dossier.

**Syntaxe** : `os.mkdir(chemin_dossier)`

**Attention** : Provoque une erreur si le dossier existe déjà.

**Exemple** :

```python
import os
os.mkdir("mon_dossier")
```

##### `os.listdir()`

Liste les fichiers et dossiers dans un dossier.

**Syntaxe** : `os.listdir(chemin_dossier)`

**Exemple** :

```python
import os
fichiers = os.listdir(".")
print(fichiers)
```

#### D.5. Module datetime

##### `datetime.datetime.now()`

Renvoie la date et l’heure actuelles.

**Exemple** :

```python
import datetime
maintenant = datetime.datetime.now()
print(maintenant)  # ex: 2025-06-16 14:30:00.123456
```

##### `datetime.datetime.strptime()`

Convertit une chaîne de caractères en objet datetime selon un format donné.

**Syntaxe** : `datetime.datetime.strptime(chaine, format)`

**Exemple** :

```python
date_str = "2025-06-16 14:30"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
```

##### `datetime.datetime.strftime()`

Convertit un objet datetime en chaîne selon un format donné.

**Syntaxe** : `date.strftime(format)`

**Exemple** :

```python
maintenant = datetime.datetime.now()
date_str = maintenant.strftime("%d/%m/%Y %H:%M")
print(date_str)  # ex: "16/06/2025 14:30"
```

##### `datetime.timedelta`

Représente une durée (différence entre deux dates).

**Utilisation** : Permet d’ajouter ou soustraire du temps à une date.

**Exemple** :

```python
from datetime import datetime, timedelta
demain = datetime.now() + timedelta(days=1)
```

## E. Notes supplémentaires

**Méthodes** : Si c’est **appelé avec un point (.)** sur un objet : **→ c’est une méthode**

**Fonctions** : Si c’est **appelé sans point** (et souvent défini globalement ou importé) : **→ c’est une fonction**





# >>> A ranger dans re

## 🧩 REGEX — Création des motifs

### 🔹 Répétitions

- `*` → 0 ou plusieurs fois  
  Ex. `a*` correspond à "", "a", "aaa"
- `+` → 1 ou plusieurs fois  
  Ex. `a+` correspond à "a", "aa"
- `?` → 0 ou 1 fois  
  Ex. `a?` correspond à "" ou "a"
- `{n}` → exactement n fois  
  Ex. `a{3}` → "aaa"
- `{n,}` → n fois ou plus  
  Ex. `a{2,}` → "aa", "aaa", …
- `{n,m}` → entre n et m fois  
  Ex. `a{2,4}` → "aa", "aaa", "aaaa"

---

### 🔹 Caractères et classes

- `.` → n’importe quel caractère sauf `\n`
- `[abc]` → un caractère parmi a, b ou c
- `[^abc]` → tout sauf a, b ou c
- `[a-z]` → une minuscule
- `[0-9]` → un chiffre

---

### 🔹 Abrégés usuels

- `\d` → chiffre `[0-9]`
- `\D` → non-chiffre
- `\w` → lettre, chiffre ou `_`
- `\W` → tout sauf \w
- `\s` → espace, tab, retour ligne
- `\S` → tout sauf un espace

---

### 🔹 Groupes et alternatives

- `(abc)` → groupe capturant
- `(?:abc)` → groupe non capturant
- `a|b` → "a" ou "b"
- `(ab|cd)` → "ab" ou "cd"

---

### 🔹 Ancres (début/fin/mot)

- `^` → début de chaîne
- `$` → fin de chaîne
- `\b` → bord de mot
- `\B` → pas bord de mot

---

### 🔹 Exemples utiles

- Nombre entier : `^\d+$`
- Mot simple (lettres/chiffres/_) : `^\w+$`
- Email très simple : `^\w+@\w+\.\w+$`
- Code postal FR : `^\d{5}$`
- Tel FR (simplifié) : `^0[1-9](\s?\d{2}){4}$`
- Mot commençant par "a" : `\ba\w*`

---

### 🔹 ➕ BONUS : nombre dans un intervalle

- ⚠️ Les regex **ne savent pas comparer des valeurs** (ex : "entre 5 et 37")  
  Il faut :

  - soit **utiliser des alternatives à la main** (ex : `0[5-9]|1[0-9]|2[0-9]|3[0-7]`)

  - soit **filtrer en Python** après un match avec `int()`  

    ```python
    if 5 <= int(valeur) <= 37:
        # OK
    ```

# >>> A ranger dans fonctions et méthodes // Comment bien commenter ses fonctions en Python (docstrings)

## Structure standard (Google style)

```python
def function_name(arg1, arg2):
    """
    Brief description of what the function does.

    Args:
        arg1 (type): Clear description of the first argument.
        arg2 (type): Clear description of the second argument.

    Returns:
        type: Description of the returned value.

    Raises:
        ExceptionType: Description of possible exceptions (if applicable).
    """
    pass
```

---

## Conseils pratiques

- La première ligne doit être courte, claire et au présent (ex. "Calculate sum of...").
- Dans Args, indiquer **nom**, **type**, et **rôle** de chaque paramètre.
- Dans Returns, préciser le **type** et la signification de la valeur retournée.
- Omettre `Raises` si aucune exception n’est levée.
- Ajouter une section `Notes` ou `Side effects` si la fonction fait des interactions ou autres effets secondaires.
- Mettre des commentaires dans le corps pour expliquer les étapes complexes.

---

## Exemple d’une fonction simple

```python
def add_numbers(a, b):
    """
    Return the sum of two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b
```

---

## Exemple avec interaction utilisateur et sauvegarde

```python
def add_client(client_database):
    """
    Add a new client to the client database by collecting user input.

    Args:
        client_database (list of dict): List of client records.

    Returns:
        list of dict: Updated client database with the new client appended.

    Notes:
        This function prompts the user for client details via input,
        validates phone, email, and birth date,
        and saves the updated database to disk.
    """
    pass
```

---

## Qu’est-ce qu’un snippet ?

Un **snippet** est un morceau de code pré-écrit insérable rapidement dans un éditeur via un raccourci clavier.  
Il permet de gagner du temps et d’uniformiser la structure des commentaires ou du code répétitif.

---

## Pourquoi commenter ses fonctions ?

- Pour rendre le code **plus lisible et compréhensible**.
- Faciliter la **maintenance** et la **collaboration**.
- Permettre une meilleure **documentation automatique** avec des outils (ex: Sphinx).
- Se souvenir du fonctionnement ou des spécificités de la fonction, même après plusieurs mois.

---

Tu veux que je te génère ce fichier en `.md` pour que tu puisses le télécharger ?  
Ou tu souhaites un PDF ?  
