from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django_photobooth_widget.widgets import PhotoboothWidget, PhotoboothModelField

class Selfie(models.Model):
    #photo = PhotoBoothField(widget=PhotoBoothWidget, required=False)
    photo = PhotoboothModelField(null=True, editable=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    your_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('index')