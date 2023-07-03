from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('medecin_details/<int:id>/',views.medecin_details, name='medecin_details'),

]
