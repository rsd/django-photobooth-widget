import django

from django import forms
from django.views.generic import FormView
from django.forms.fields import CharField

#from charsleft_widget import CharsLeftArea


class TestForm(forms.Form):
    #field = CharField(max_length=128, widget=CharsLeftArea)
    field = CharField(max_length=128)


class TestView(FormView):
    form_class = TestForm
