""" Modelos de la app usuarios """
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


class Avatar(models.Model):
    """ Clase que representa un avatar """
    nombre_imagen = models.CharField(max_length=20, blank=False)
    nombre_a_mostrar = models.CharField(max_length=20, blank=False)
    descripcion = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre_a_mostrar


class User(AbstractUser):
    """ Clase que sobreescribe el usuario que utiliza django por defecto,
    agregando algunos campos extra"""
    # Importo los paises de un .txt
    paises = []
    file1 = open('users/resources/paises.txt', 'r')
    count = 0
    for line in file1:
        count += 1
        paises.append((line.replace("\n", ""), line.replace("\n", "")))
    file1.close()
    biografia = models.TextField(max_length=500, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    intereses = models.CharField(max_length=100, blank=True)
    pais = models.CharField(choices=paises,
                            max_length=50,
                            null=True,
                            blank=True)
    avatar = models.ForeignKey(Avatar,
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True)
