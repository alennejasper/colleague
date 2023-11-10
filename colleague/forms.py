from django import forms
from django.forms import ModelForm
from django.forms.widgets import FileInput
from .models import Classmate

class ClassmateForm(ModelForm):
    class Meta:
        model = Classmate
        fields = "__all__"
        widgets = {"profile_photo": FileInput()}
