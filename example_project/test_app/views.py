import django

from django import forms
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_photobooth_widget.widgets import PhotoboothModelField, PhotoboothWidget
from django.views import generic
from .models import Selfie

from .models import Selfie

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_selfies = Selfie.objects.all().count()

    context = {
        'num_selfies': num_selfies,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'test_app/index.html', context=context)

class SelfieDetailView(generic.DetailView):
    model = Selfie
    context_object_name = "selfie"

class SelfieCreateView(generic.CreateView):
    model = Selfie
    context_object_name = "my_new_selfie"
    fields = ['photo', 'title', 'description', 'your_name']


class SelfieListView(generic.ListView):
    model = Selfie
    context_object_name = 'selfie_list'





class TestForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    #photo = PhotoBoothField(widget=PhotoBoothWidget, required=False)


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