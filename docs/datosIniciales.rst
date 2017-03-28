Para generar
############

.. Code::

  /Rapidito> ./manage.py dumpdata -v 3 --indent 3 factura.empresa > rapidito/datosIniciales/empresas.json
  /Rapidito> ./manage.py dumpdata -v 3 --indent 3 factura.autorización > rapidito/datosIniciales/autorización.json


Para Capgar los datos
#####################

.. Code::

  /Rapidito> ./manage.py loaddata empresas
  /Rapidito> ./manage.py loaddata autorización