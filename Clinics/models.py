from django.db import models


# # Create your models here.


class Clinique(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='clinique_images/')
    tele = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
