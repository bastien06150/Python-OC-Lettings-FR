Sentry
======

Sentry est utilisé pour surveiller les erreurs de l'application en production.

Configuration
-------------

La configuration Sentry est réalisée dans le fichier ``settings.py``.

La variable d'environnement utilisée est :

.. code-block:: text

   SENTRY_DSN

Utilité
-------

Sentry permet de :

* capturer les erreurs en production ;
* suivre les exceptions Django ;
* consulter les logs applicatifs ;
* faciliter le diagnostic des bugs.