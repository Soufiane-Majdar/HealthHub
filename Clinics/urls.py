from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cliniques/<int:clinique_id>/', views.clinique_details, name='clinique_details'),
]
