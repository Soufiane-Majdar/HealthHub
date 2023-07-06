from django.shortcuts import render, redirect
from .models import RendezVous
from Clinics.models import Clinique
from Users.models import *

# Create your views here.


from django.shortcuts import render, redirect
from .models import RendezVous, Clinique, Medecin, Patient

import uuid


def appointment_success(request):
    return redirect(to='home')


def generate_code():
    # Generate a code that is unique for RenderVous code field
    while True:
        code = str(uuid.uuid4().hex)[:8]
        if not RendezVous.objects.filter(code=code).exists():
            break
    return code


def make_appointment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        patient = request.POST.get('patient')
        patient_id = Patient.objects.get(username=patient).id
        medecin_id = request.POST.get('medecin')
        clinique_id = request.POST.get('clinique')
        specialite = request.POST.get('specialite')

        code = generate_code()

        rendezvous = RendezVous.objects.create(
            date=date,
            time=time,
            patient_id=patient_id,
            medecin_id=medecin_id,
            clinique_id=clinique_id,
            specialite=specialite,
            code=code,
            status='pending'
        )

        # Handle any additional logic or redirect to a success page
        return redirect('appointment_success')

    patients = Patient.objects.all()
    medecins = Medecin.objects.all()
    cliniques = Clinique.objects.all()
    return render(request, 'clinic/make_appointment.html', {'patients': patients, 'medecins': medecins, 'cliniques': cliniques})
