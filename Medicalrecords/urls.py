from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('make-appointment/', views.make_appointment, name='make_appointment'),
]
