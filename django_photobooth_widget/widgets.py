from django.db import models
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
import base64

PHOTOBOOTH_DATASTREAM_PREFIX="data:image/png;base64"

#TODO: make this flag per instance
PHOTOBOOTH_DB_SAVE_AS_BINARY=True

class PhotoboothImage():
    def __init__(self, image=None):
        self._base64_image = None
        self._raw_image = None
        self.has_image = False

        if image is not None:
            if isinstance(image,str):
                self.base64_image(image)
            elif isinstance(image, bytes):
                self.raw_image(image)

    def base64_image(self, base64_image=None):
        if base64_image is not None:
            if isinstance(base64_image, str):
                photo = base64_image.split(",")
                if photo[0] == PHOTOBOOTH_DATASTREAM_PREFIX:
                    base64_image = photo[1]

                #TODO: have to validate base64
                self._raw_image = base64.b64decode(base64_image)
                self._base64_image = PHOTOBOOTH_DATASTREAM_PREFIX + "," + base64_image
                self.has_image = True
            elif isinstance(base64_image, bytes):
                self.raw_image(base64_image)
        return self._base64_image

    def raw_image(self, raw_image=None):
        if raw_image is not None:
            if isinstance(raw_image, bytes):
                self._raw_image = raw_image
                self._base64_image = PHOTOBOOTH_DATASTREAM_PREFIX + "," + base64.b64encode(raw_image).decode()
                self.has_image = True
            elif isinstance(raw_image, str):
                self.base64_image(raw_image)
        return self._raw_image


# Model Field

# FIXME: Transform in a ImageField
class PhotoboothModelField(models.BinaryField):

    description = "A photo taken by the device camera"

    def __init__(self, *args, **kwargs):
        kwargs['editable'] = True
        super().__init__(*args, **kwargs)
        self.photobooth = PhotoboothImage()

    def __str__(self):
        return "Photobooth Image Field"

    def formfield(self, **kwargs):
        defaults = {'form_class': PhotoboothFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def _convert_to_photobooth(self, value):
        photobooth = PhotoboothImage()
        if PHOTOBOOTH_DB_SAVE_AS_BINARY:
            photobooth.raw_image(value)
        else:
            photobooth.base64_image(value)
        self.photobooth = photobooth
        return photobooth

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self._convert_to_photobooth(value)

    def to_python(self, value):
        if isinstance(value, PhotoboothImage):
            return value
        if value is None:
            return value
        return self._convert_to_photobooth(value)

    def get_prep_value(self, photobooth):
        if PHOTOBOOTH_DB_SAVE_AS_BINARY:
            return photobooth.raw_image()
        else:
            return photobooth.base64_image()


# Form Field
class PhotoboothFormField(forms.Field):

    def __init__(self, *args, **kwargs):
        defaults = {}
        defaults.update(kwargs)
        if "max_length" in defaults:
            del defaults["max_length"]
            print("deleting defaults")

        super().__init__(*args, **defaults)
        self.widget = PhotoboothWidget()

# Widget
class PhotoboothWidget(forms.Widget):
    template_name = "photobooth_widget/photobooth_widget.html"

    class Media:
        css = {
            'screen': (
                staticfiles_storage.url(
                    'photobooth_widget/css/photobooth_widget.css',
                    ),
                )}
        js = ( staticfiles_storage.url('photobooth_widget/js/photobooth_min.js'),
               staticfiles_storage.url('photobooth_widget/js/photobooth_activate.js'),
              )

    def __init__(self, attrs=None, *args, **kwargs):
        attrs = attrs or {}
        super().__init__(attrs)
    

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        output = render_to_string(self.template_name, {"name": name, "value": value})
        return mark_safe(output)