CI/CD
=====

Le projet utilise GitHub Actions pour automatiser les vérifications du code.

Pipeline
--------

À chaque push sur GitHub, le pipeline exécute :

* l'installation des dépendances ;
* l'analyse du code avec Flake8 ;
* les tests automatisés avec Pytest ;
* la vérification de la couverture de tests.

Lien du pipeline
----------------

Le pipeline est accessible depuis l'onglet Actions du dépôt GitHub :

.. code-block:: text

   https://github.com/bastien06150/Python-OC-Lettings-FR/actions