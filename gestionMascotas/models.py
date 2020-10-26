from django.db import models

# Create your models here.
class Mascota(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return "Código: {} \n" \
               "Nombre: {} \n" \
               "Raza: {} \n" \
               "edad: {}".format(self.codigo,self.nombre,self.raza, self.edad)




