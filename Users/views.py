from django.shortcuts import render, HttpResponse, redirect


# Face-recognitions
import cv2
import numpy as np
import face_recognition
import os

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


############ Face-recognitions login ############
def face_login(user):
    path = 'media/medecin_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    names = ""
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                # multiply by 4 to get the original size of the image
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name+", Allowed", (x1+6, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                print(name)
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(1) & 0xFF

                # print(k)
                if name == user.upper():
                    # close the webcam
                    cv2.destroyAllWindows()
                    return True
                elif name != "":
                    cv2.destroyAllWindows()
                    return False
                elif k == ord('q'):
                    # close the webcam if the user click on 'q':
                    cv2.destroyAllWindows()
                    return False

############ end Face-recognitions login ############


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
                # check role of the user and add it to session
                if check_user[0].role == "medecin" and face_login(check_user[0].nom) == True:

                    request.session['USER'] = {
                        'id': check_user[0].id, 'email': check_user[0].email, 'role': check_user[0].role}
                    return redirect('home')
                elif check_user[0].role == "admin":
                    request.session['USER'] = {
                        'id': check_user[0].id, 'email': check_user[0].email, 'role': check_user[0].role}
                    return redirect('home')
                elif check_user[0].role == "patient":
                    request.session['USER'] = {
                        'id': check_user[0].id, 'email': check_user[0].email, 'role': check_user[0].role}
                    return redirect('home')
                else:
                    title = "Login"

                    message = [
                        'You are not allowed to login here!, you must make a face login.', 'danger']
                    return render(request, 'users/login.html', {'title': title, 'message': message})

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


def profile(request):
    if 'USER' in request.session:
        title = "Profile"
        print(request.session['USER'])
        return render(request, 'users/profile.html', {'title': title})
    else:
        title = "Home"
        return render(request, 'home/home.html', {'title': title})


def Host(request):
    title = "Host"
    return render(request, 'host/becam_host.html', {'title': title})
