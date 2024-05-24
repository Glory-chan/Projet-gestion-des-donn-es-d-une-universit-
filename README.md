# Titre du Projet :

# Gestion des données d’une université.

### Description :

Ce projet consiste à  créer une base de données mongoDB et quelques fonctions
en python pour gérer et manipuler les données issues de la base de données de l'université.

### Prérequis :

- Python 3.8+
- MongoDB
- Bibliothèques Python : pymongo, bson

### Installation :

- pip install pymongo
- pip install bson

### Configuration :

Installation des dépendances :

Utilisez pip pour installer les dépendances Python répertoriées dans le fichier requirements.txt. Exécutez la commande suivante dans votre environnement virtuel :

- pip install -r requirements.txt

Configuration de la base de données :

- Assurez-vous que MongoDB est installé et en cours d'exécution sur votre système.
- Vérifiez que les informations de connexion à la base de données sont correctes dans le fichier database.py de votre projet.

Créer le répertoire de données
Vous devez créer le répertoire où MongoDB stockera ses données. Par défaut, c'est C:\data\db sur Windows.

Ouvrez l'Explorateur de fichiers.
Allez à C:.
Créez un nouveau dossier appelé data.
Dans le dossier data, créez un autre dossier appelé db.
Vous pouvez également le faire à partir de la ligne de commande :

- mkdir C:\data
- mkdir C:\data\db

Démarrer MongoDB dans votre terminal avec la commande :

- mongod

Exécution de l'application :

- Assurez-vous d'être dans le répertoire racine de votre projet.
- Exécutez le fichier main.py à l'aide de la commande suivante :
   - python main.py

Utilisation de l'application :

Suivez les instructions affichées dans la console pour interagir avec l'application et effectuer différentes opérations de gestion universitaire.


### Utilisation :

1. Exécuter le script main.py pour lancer l'application.
2. Suivre les instructions à l'écran pour interagir avec le menu.
3. Choisissez l'option correspondante pour ajouter des données, par exemple:
   - Pour ajouter une faculté, appuyez sur 1 et suivez les instructions.

### Fonctionnalités :

1. Ajouter une faculté : Permet d'ajouter une nouvelle faculté avec un nom et une description.

2. Ajouter une école : Permet d'ajouter une nouvelle école avec un nom et une description.

3. Ajouter un programme : Permet d'ajouter un nouveau programme avec un nom, en spécifiant l'ID de la faculté à laquelle il est associé, et éventuellement l'ID de l'école.

4. Ajouter une unité d'enseignement (UE) : Permet d'ajouter une nouvelle UE avec un nom, une description, en spécifiant l'ID de la faculté à laquelle elle est associée, et éventuellement l'ID de l'école.

5. Ajouter un enseignant : Permet d'ajouter un nouvel enseignant avec un nom, un email, en spécifiant l'ID de la faculté à laquelle il est associé, et éventuellement l'ID de l'école.

6. Ajouter un étudiant : Permet d'ajouter un nouvel étudiant avec un nom, un email et en spécifiant l'ID du programme auquel il est inscrit.

7. Ajouter un membre du personnel administratif : Permet d'ajouter un nouveau membre du personnel administratif avec un nom, un email, en spécifiant l'ID de la faculté à laquelle il est associé, et éventuellement l'ID de l'école.

8. Ajouter une inscription : Permet d'ajouter une nouvelle inscription en spécifiant l'ID de l'étudiant, l'ID de l'UE et le semestre.

9. Voir le nombre d'étudiants inscrits par UE : Affiche le nombre d'étudiants inscrits pour chaque UE.

### Contribution :

Si vous êtes ouvert aux contributions de tiers, indiquez comment ils peuvent contribuer à votre projet. Incluez des instructions pour soumettre des pull requests, des règles de code ou des directives spécifiques.

### Licence :

Indiquez la licence sous laquelle votre projet est distribué. Cela informe les utilisateurs de ce qu'ils peuvent et ne peuvent pas faire avec votre code.

Ce projet est licencié sous la licence MIT - voir le fichier LICENSE.md pour plus de détails.
