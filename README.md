# Application Web Planning Poker

Cette application permet de jouer au **Planning Poker** en ligne, permettant à plusieurs participants d'estimer la difficulté des fonctionnalités d'un projet. Les règles sont flexibles (strict, moyenne, médiane, etc.) et l'application génère un fichier JSON avec les résultats à la fin.

## Fonctionnalités

- **Création de joueurs** : Permet de définir des joueurs avec des rôles (admin ou non).
- **Création de parties** : Sélection des participants et de l'admin pour chaque partie.
- **Vote de fonctionnalités** : Chaque joueur vote avec une carte, et les votes sont validés selon les règles choisies.
- **Mode de jeu** : Strict, moyenne, médiane, etc.
- **Gestion des parties** : Suivi de l'état des parties (en cours, terminé, non commencé).
- **Export JSON** : Sauvegarde des résultats des votes et des fonctionnalités dans un fichier JSON.
- **Reprise de la partie** : Reprise d'une partie en cours à partir d'un fichier JSON sauvegardé.

## Installation

# **Instructions pour exécuter le projet Django**

## **Prérequis**

1. Assurez-vous que les éléments suivants sont installés sur votre machine :
   - **Python** (version 3.7 ou plus récente)
   - **pip** (le gestionnaire de paquets Python)
   - **virtualenv** (optionnel mais recommandé)

2. Téléchargez ou clonez le projet depuis GitHub :
   ```bash
   git clone https://github.com/Abdeldjebbar10/POKER_PROJECT.git
   cd POKER_PROJECT
# Clonez le dépôt
git clone https://github.com/Abdeldjebbar10/POKER_PROJECT.git
cd POKER_PROJECT

# Créez et activez l'environnement virtuel
pour creer : 
python -m venv env     


pour activer :   
Sur Windows :  
env\Scripts\activate  
Sur macOS/Linux :  
source env/bin/activate


# Installez les dépendances
pip install -r requirements.txt

# Configurez la base de données

python manage.py makemigrations

python manage.py migrate    

python manage.py createsuperuser  # Optionnel

# Lancez le serveur
python manage.py runserver

#  Ajout de fichiers pour la création de parties
Lors de la création d'une partie, il est nécessaire d'uploader un fichier .JSON ou txt contenant les détails des fonctionnalités. Par exemple :



[


    {
        "id": 20,  
        
        "name": "Authentification des utilisateurs ",     
        
        "description": "Permettre à un utilisateur de se connecter avec un email et un mot de passe ."    
        
    },   
    
    {
        "id": 21,    
        
        "name": "Création d'une page de profil ",    
        
        "description": "Permettre aux utilisateurs de visualiser et modifier leurs informations personnelles."    
        
    },   
    
    {    
        "id": 22,   
        
        "name": "Gestion des notifications ",    
        
        "description": "Envoyer des notifications par email aux utilisateurs pour les événements importants ."   
        
    }


    
]

Vous pouvez utiliser des fichiers avec les extensions suivantes :

.js
.txt
on a testé et fonctionnel avec ces deux formats.



#  Pour exécuter le serveur Doxygen et voir les documents générés, suivez ces étapes :
python -m http.server
#  Lancer un serveur pour voir la documentation :
Ouvrez votre navigateur et allez à l'adresse http://localhost:8000/docs pour voir la documentation.























