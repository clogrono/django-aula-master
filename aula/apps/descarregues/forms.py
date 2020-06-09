"""
    Forms for the descarrega app
""" 
from django import forms
from .utils import composa_opcions_grups

class descarregaAlumnesForm(forms.Form):
    tutors = forms.CharField(label="Quins tutors?",
                           widget=forms.SelectMultiple(
                               choices=composa_opcions_grups()
                               ))