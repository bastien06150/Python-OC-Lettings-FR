Déploiement
===========

L'application est déployée sur Render à partir d'une image Docker publiée sur Docker Hub.

Docker Hub
----------

L'image Docker est publiée avec les commandes suivantes :

.. code-block:: bash

   docker tag oc-lettings bastienm06/oc-lettings:latest
   docker push bastienm06/oc-lettings:latest

Render
------

Render récupère l'image Docker depuis Docker Hub :

.. code-block:: text

   docker.io/bastienm06/oc-lettings:latest

Variables d'environnement Render
--------------------------------

Les variables utilisées sur Render sont :

.. code-block:: text

   SECRET_KEY
   SENTRY_DSN
   DEBUG
   ALLOWED_HOSTS
   PORT

URL de production
-----------------

L'application est accessible à l'adresse :

.. code-block:: text

   https://oc-lettings-latest-4lna.onrender.com