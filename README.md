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






























