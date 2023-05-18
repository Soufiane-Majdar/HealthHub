from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import Clinique


def home(request):
    cliniques = Clinique.objects.all()
    for clinique in cliniques:
        print("============================================================================\n\n")
        print("Nom:", clinique.nom)
        print("Adresse:", clinique.adresse)
        print("Description:", clinique.description)
        print("Image:", clinique.image.url)  # Assuming image field is not null
        print("Tele:", clinique.tele)
        print("Email:", clinique.email)

    return render(request, 'index.html')
