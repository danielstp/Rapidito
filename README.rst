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
