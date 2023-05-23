from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from Clinics.models import Clinique
from .models import *


############ Logout form Session ############
def logout(request):
    try:
        del request.session['USER']
    except:
        return redirect('login')
    return redirect('home')
############ end Logout form Session ############


def login(request):
    if 'USER' in request.session:
        return redirect('home')
    else:
        # Check if the data is Posted
        if (request.POST):
            # check if user exists
            check_user = User.objects.filter(
                email=request.POST['email'], password=request.POST['password'])
            if check_user:
                # print(check_user[0].userName)

                # Add User to Session

                # uname=str(check_user[0].userName)
                request.session['USER'] = {
                    'role': check_user[0].role,
                    'userName': check_user[0].username,
                    'fName': check_user[0].prenom,
                    'lName': check_user[0].nom,
                    'email': check_user[0].email
                }

                title = "Login"
                message = ['hello '+request.session['USER']
                           ['role']+" "+request.session['USER']
                           ['userName'], 'success']
                # return render(request, 'users/login.html', {'title': title, 'message': message})
                return redirect('home')

            else:
                # User not found email or psss word incorect:
                title = "Login"
                message = ['email or psss incorect!', 'danger']
                return render(request, 'users/login.html', {'title': title, 'message': message})
        # if it's not Post method
        else:
            title = "Login"
            return render(request, 'users/login.html', {'title': title})
############ end Login to Session ###########


def signup(request):
    cliniques = Clinique.objects.all()
    medecins = Medecin.objects.all()

    return render(request, 'users/signup.html', {"medecins": medecins, "cliniques": cliniques})
