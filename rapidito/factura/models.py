from django.db import models


class Empresa(models.Model):
  nit = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=255)


class Autorizacion(models.Model):
  autorizacion = models.IntegerField(primary_key=True)
  nit = models.ForeignKey(Empresa)


class Factura(models.Model):
  autorizacion = models.ForeignKey(Autorizacion)
  #  nit          = models.IntegerField()
  factura      = models.IntegerField()
  fecha        = models.DateField()
  importe      = models.DecimalField(decimal_places=2,max_digits=10)
  control      = models.IntegerField()


class Tipo_de_formulario(models.Model):
  codigo = models.CharField(max_length=10)
  nombre = models.CharField(max_length=255)
