Installation
============

Prérequis
---------

Le projet nécessite :

* Python 3.11
* Git
* Docker Desktop
* Make

Cloner le projet
----------------

.. code-block:: bash

   git clone https://github.com/bastien06150/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Créer l'environnement virtuel
-----------------------------

.. code-block:: bash

   python -m venv env
   env\Scripts\activate

Installer les dépendances
-------------------------

.. code-block:: bash

   pip install -r requirements.txt

Variables d'environnement
-------------------------

Créer un fichier ``.env`` à la racine du projet :

.. code-block:: text

   SECRET_KEY=votre_secret_key
   SENTRY_DSN=votre_dsn_sentry

Lancer le serveur local
-----------------------

.. code-block:: bash

   python manage.py runserver