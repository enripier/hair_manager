Voici le cahier des charges pour ton nouvel exercice Python de niveau 3 :

🗓️ Projet : Agenda de Rendez-vous (console)

🎯 Objectif

Créer une application console permettant de gérer un agenda personnel :
	•	Ajout, modification, suppression de rendez-vous
	•	Consultation par date ou période
	•	Sauvegarde automatique en JSON

⸻

✅ Fonctionnalités de base
	1.	Ajouter un rendez-vous
	•	Champs : titre, date, heure, durée, description (optionnelle)
	•	Contrôle : format de date/heure, pas de doublons
	2.	Modifier un rendez-vous
	•	Par sélection du rendez-vous via son identifiant ou sa date/heure
	•	Possibilité de modifier un ou plusieurs champs
	3.	Supprimer un rendez-vous
	•	Par identifiant, ou liste filtrée avec confirmation
	4.	Afficher les rendez-vous
	•	Tous les rendez-vous triés par date
	•	Par jour, semaine ou mot-clé
	•	Affichage clair (date, heure, titre, durée…)
	5.	Sauvegarde automatique
	•	Les rendez-vous sont stockés dans un fichier agenda.json
	•	Chargement automatique au démarrage

⸻

💡 Extensions possibles plus tard
	•	Détection de conflit (deux rendez-vous au même moment)
	•	Export du planning d’un jour donné dans un fichier .txt
	•	Affichage coloré ou encadré (avec rich ou tabulate)
	•	Recherche par mot-clé ou date partielle

⸻

🧰 Modules Python à utiliser
	•	json → sauvegarde/chargement
	•	datetime → gestion des dates et heures
	•	os ou pathlib → vérifier si le fichier existe
	•	input() + boucles → interface console simple

⸻

🧪 Étapes de travail
	1.	Créer une structure pour stocker un rendez-vous (dictionnaire)
	2.	Gérer une liste de rendez-vous en mémoire
	3.	Créer des fonctions : ajouter, supprimer, modifier, afficher
	4.	Gérer la sauvegarde automatique (lecture/écriture JSON)
	5.	Ajouter un menu principal avec boucle while et choix utilisateur