from django.db import models

from Clinics.models import Clinique
from Users.models import *


# Create your models here.


class RendezVous(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='patient')
    medecin = models.ForeignKey(
        Medecin, on_delete=models.CASCADE, related_name='medecin')
    clinique = models.ForeignKey(
        Clinique, on_delete=models.CASCADE, related_name='clinique')
    specialite = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, default='pending')
    pdf = models.FileField(upload_to='media/rendezvous_pdfs/', blank=True)

    def __str__(self):
        return self.code


class Ordonnance(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='ordonnance_patient')
    medecin = models.ForeignKey(
        Medecin, on_delete=models.CASCADE, related_name='ordonnance_medecin')
    clinique = models.ForeignKey(
        Clinique, on_delete=models.CASCADE, related_name='ordonnance_clinique')
    observation = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    diagnostic = models.TextField(blank=True)
    pdf = models.FileField(upload_to='media/ordonnance_pdfs/', blank=True)

    def __str__(self):
        return self.patient.nom


class DossierMedical(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='dossier_patient')
    medecin = models.ForeignKey(
        Medecin, on_delete=models.CASCADE, related_name='dossier_medecin')
    clinique = models.ForeignKey(
        Clinique, on_delete=models.CASCADE, related_name='dossier_clinique')
    ordonnance = models.ForeignKey(
        Ordonnance, on_delete=models.CASCADE, related_name='dossier_ordonnance')
    Maladie = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.patient.nom
