from django.db import models


class Empresa(models.Model):
    nit = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre + ", " + str(self.nit)


class Autorización(models.Model):
    autorización = models.BigIntegerField(primary_key=True)
    nit = models.ForeignKey(Empresa)

    def __str__(self):
        return self.nit.nombre + ", " + str(self.autorización)

    class Meta:
        verbose_name_plural = "Autorizaciones"


class Factura(models.Model):
    autorización = models.ForeignKey(Autorización)
    # nit = models.IntegerField()
    factura = models.IntegerField()
    fecha = models.DateField()
    importe = models.DecimalField(decimal_places=2, max_digits=10)
    control = models.CharField(max_length=128)
