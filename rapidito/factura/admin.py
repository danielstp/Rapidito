from django.contrib import admin

from .models import Empresa
from .models import Autorizacion
from .models import Factura

admin.site.register(Empresa)
admin.site.register(Autorizacion)
admin.site.register(Factura)
