from django.db import models

from Clinics.models import *


# Create your models here.


class User(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    tele = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username


class Admin(User):
    # define role as admin
    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.role = 'admin'


def upload_to(instance, filename):
    user_name = instance.nom
    new_filename = f"{user_name}.jpg"
    return f"media/medecin_images/{new_filename}"


class Medecin(User):
    SPECIALITES_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('gastroenterology', 'Gastroenterology'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('ophthalmology', 'Ophthalmology'),
        ('pediatrics', 'Pediatrics'),
        ('psychiatry', 'Psychiatry'),
        ('urology', 'Urology'),
        ('others', 'Others'),
    ]
    specialite = models.CharField(max_length=255, choices=SPECIALITES_CHOICES)
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, blank=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    jours_disponible = models.CharField(max_length=255)
    heure_disponible = models.CharField(max_length=255)

    # define role as medecin
    def __init__(self, *args, **kwargs):
        super(Medecin, self).__init__(*args, **kwargs)
        self.role = 'medecin'
        #  Modify the filename here so that it includes the user "nom"  exemple: "nom.jpg"


class Secretaire(User):
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)
    # define role as secretaire

    def __init__(self, *args, **kwargs):
        super(Secretaire, self).__init__(*args, **kwargs)
        self.role = 'secretaire'


class Patient(User):
    # sexe choices
    SEXE_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]

    address = models.CharField(max_length=255, blank=True)
    sexe = models.CharField(max_length=255, choices=SEXE_CHOICES, blank=True)
    date_naissance = models.DateField(blank=True, null=True)

    # define role as patient
    def __init__(self, *args, **kwargs):
        super(Patient, self).__init__(*args, **kwargs)
        self.role = 'patient'
