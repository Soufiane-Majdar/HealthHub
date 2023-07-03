from django.shortcuts import render, redirect
from .models import RendezVous
from Clinics.models import Clinique
from Users.models import *

# Create your views here.


from django.shortcuts import render, redirect
from .models import RendezVous, Clinique, Medecin, Patient


def make_appointment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        patient_id = None
        medecin_id = None

        # Check if the user is a patient or a medecin
        if 'USER' in request.session and request.session['USER']['role'] == "patient":
            # Check if the patient is logged in
            if 'USER' in request.session and 'id' in request.session['USER']:
                patient_id = request.session['USER']['id']
            else:
                email = request.POST.get('email')
                password = request.POST.get('password')

                # Check if the patient exists in the database
                try:
                    patient = Patient.objects.get(
                        email=email, password=password)
                    patient_id = patient.id
                except Patient.DoesNotExist:
                    # Patient not found, handle the error or redirect to an appropriate page
                    return render(request, 'clinic/make_appointment.html', {'cliniques': Clinique.objects.all()})
        elif 'USER' in request.session and request.session['USER']['role'] == "medecin":
            # Check if the medecin is logged in
            if 'USER' in request.session and 'id' in request.session['USER']:
                medecin_id = request.session['USER']['id']
            else:
                email = request.POST.get('email')
                password = request.POST.get('password')

                # Check if the medecin exists in the database
                try:
                    medecin = Medecin.objects.get(
                        email=email, password=password)
                    medecin_id = medecin.id
                except Medecin.DoesNotExist:
                    # Medecin not found, handle the error or redirect to an appropriate page
                    return render(request, 'clinic/make_appointment.html', {'cliniques': Clinique.objects.all()})
        else:
            # Invalid role, handle the error or redirect to an appropriate page
            return render(request, 'clinic/make_appointment.html', {'cliniques': Clinique.objects.all()})

        clinique_id = request.POST.get('clinique')
        specialite = request.POST.get('specialite')

        # Create the appointment
        rendezvous = RendezVous.objects.create(
            date=date,
            time=time,
            patient_id=patient_id,
            medecin_id=medecin_id,
            clinique_id=clinique_id,
            specialite=specialite,
            status='pending'
        )

        # Handle any additional logic or redirect to a success page
        return redirect('appointment_success')

    # GET request or invalid form submission
    return render(request, 'clinic/make_appointment.html', {'cliniques': Clinique.objects.all()})
