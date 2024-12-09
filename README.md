# Flask Application

## Installation

1. Clonez le dépôt de l'application.
2. Créez un environnement virtuel et activez-le :
    ```sh
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```
3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Lancement de l'application

1. Assurez-vous que l'environnement virtuel est activé.
2. Lancez l'application :
    ```sh
    python app.py
    ```
3. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`.

## Fonctionnalités

- **Inscription** : Les utilisateurs peuvent s'inscrire avec un email et un mot de passe.
- **Connexion** : Les utilisateurs peuvent se connecter avec leurs identifiants.
- **Déconnexion** : Les utilisateurs peuvent se déconnecter.
- **Page d'accueil** : Une page d'accueil protégée par authentification.

## Structure du projet

- `app.py` : Le fichier principal de l'application Flask.
- `templates/` : Dossier contenant les fichiers HTML pour les différentes pages de l'application.
- `requirements.txt` : Liste des dépendances Python nécessaires pour l'application.

## Dépendances

- Flask
- Flask-WTF
- Flask-Login
- WTForms