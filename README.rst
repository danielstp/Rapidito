Rapidito
========

La Comunidad Software Libre Bolivia, tiene el objetivo de desarrollar "El Sistema de Facturación Virtual",
una aplicación Web, como alternativa al Software Privativo desarrollado por Inpuestos Nacionales del
Estado Plurinacional de Bolivia.

Esto amparado en la Ley, Decretos y pronta reglamentación de la "Migración de Software Libre en las Instituciones
del Estado Plurinacional de Bolivia", y contribuir a producir Software Libre, bajo las licencias compatibles
con GNU General Plublic License.

Install
^^^^^^^

Leer el archivo docs/install.rst para mas instrucciones.


Basic Commands
^^^^^^^^^^^^^^

Para ejecutar el servicio modo desarrollador

::
  $ python manage.py runserver

Si estas depurando

::
  $ python manage.py runnserver --noreload --nothreading

También es bueno usar el depurador pudb

::
  $ python -m pudb manage.py runserver --noreload --nothreading


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Running Linters
^^^^^^^^^^^^^^^

Es necesario ejecutar pep8, flake8, pylint para mantener el código con buenas practicas de programación.

Running pep8
~~~~~~~~~~~~~~

::
  $ pep8 rapidito

Para excluir carpetas, modificar el archivo setup.cfg

Running flake8
~~~~~~~~~~~~~~

::
  $ flake8 rapidito

Para excluir carpetas, modificar el archivo setup.cfg

Running pylint
~~~~~~~~~~~~~~

::
  $ pylint rapidito

Para excluir carpetas, modificar el archivo .pylintrc

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

Antes de ejecutar las pruebas, es necesario que revisen si el [usuario] tenga acceso
para crear base de datos. De lo contrario genera errores

::
  $ sudo -u postgres psql postgres
  postgres=# ALTER USER [username] CREATEDB;
  postgres=#\q

::
  $ py.test



Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Asegurar que nodejs esta instalado

::
  $ npm install

Instalar compass

::
  $ gem install compass

Ejecutar

::
  $ gulp runServer


Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd rapidito
    celery -A rapidito.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



