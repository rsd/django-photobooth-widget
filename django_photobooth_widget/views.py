import django

from django import forms
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .widgets import PhotoBoothField, PhotoBooth


class TestForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    photo = PhotoBoothField(widget=PhotoBooth, required=False)


class TestView(FormView):
    form_class = TestForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print ("form is valid: " + form.cleaned_data['photo'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/')
        else:
            print ("Erro validando form")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'homepage.html', {'form': form})