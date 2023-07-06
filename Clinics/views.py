from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import Clinique
from Users.models import Medecin


def home(request):
    is_a_patient = False
    if 'USER' in request.session:
        if request.session['USER']['role'] == 'patient':
            is_a_patient = True

    cliniques = Clinique.objects.all()
    medecins = Medecin.objects.all()

    return render(request, 'home.html', {"medecins": medecins, "cliniques": cliniques, "is_a_patient": is_a_patient})


#  clinique  details
def clinique_details(request, clinique_id):
    clinique = Clinique.objects.get(id=clinique_id)
    medecins_clinique = Medecin.objects.filter(clinique=clinique_id)

    return render(request, 'clinic/clinique_details.html', {"clinique": clinique, "medecins_clinique": medecins_clinique})
