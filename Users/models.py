from django.db import models

from Clinics.models import *


# Create your models here.


class User(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    tele = models.CharField(max_length=20)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Admin(User):
    pass


class Medecin(User):
    specialite = models.CharField(max_length=255)
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medecin_images/')
    description = models.TextField()
    address = models.CharField(max_length=255)
    jours_disponible = models.CharField(max_length=255)
    heure_disponible = models.CharField(max_length=255)


class Secretaire(User):
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)


class Patient(User):
    address = models.CharField(max_length=255)
    sexe = models.CharField(max_length=255)
    date_naissance = models.DateField()
