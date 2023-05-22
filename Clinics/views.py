from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import Clinique
from Users.models import Medecin


def home(request):
    cliniques = Clinique.objects.all()
    medecins = Medecin.objects.all()

    return render(request, 'index.html', {"medecins": medecins, "cliniques": cliniques})
