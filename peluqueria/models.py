from django.db import models



class Peluquero_info(models.Model):
   
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 20)
    rubro = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 9)
    email = models.EmailField()
    horario = models.CharField(max_length = 30)


# Create your models here.
