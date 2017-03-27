from django.contrib import admin

from .models import Empresa
from .models import Autorización
from .models import Factura

admin.site.register(Empresa)
admin.site.register(Autorización)
admin.site.register(Factura)
