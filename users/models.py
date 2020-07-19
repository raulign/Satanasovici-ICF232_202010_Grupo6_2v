from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    rut = models.CharField(max_length = 9, primary_key=True)
    contraseña = models.CharField(max_length = 15)
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 15)
    edad = models.IntegerField()
    telefono = models.CharField(max_length = 15)
    email = models.EmailField()



class Peluquero(models.Model):
   
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 20)
    rubro = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 9)
    email = models.EmailField()
    horario = models.CharField(max_length = 30)



