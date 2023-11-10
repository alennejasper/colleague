from django.urls import path
from . import views

urlpatterns = [
    path("colleague/create", views.ClassmatesCreate, name = "Classmates Create"),
    path("colleague/list", views.ClassmatesList, name = "Classmates List"),
    path("colleague/details/<int:id>", views.ClassmatesDetails, name = "Classmates Details"),
    path("colleague/details/delete/<int:id>", views.ClassmatesDelete, name = "Classmates Delete"),
    path("colleague/details/update/<int:id>", views.ClassmatesEdit, name = "Classmates Edit")
]
