from django.urls import path
from . import views

urlpatterns = [
    path('',views.patient, name="Patient"),
    path('<int:id>/',views.patientrecord, name="patientrecord"),
    path('<slug:id>/',views.patientrecord, name="patientrecord"),
    path('<str:id>/',views.patientrecord, name="patientrecord"),
    path('<uuid:id>/',views.patientrecord, name="patientrecord"),
]
