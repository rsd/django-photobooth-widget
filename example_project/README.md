Photobooth Widget Example Project
=================================

Test Photobooth
---------------
A. Prepare the environment.

1. Create the virtualenv:  
   `$ virtualenv -p python3 venv`  
   `$ source venv/bin/activate`

2. Add parent directory, for photobooth modules access:  
   `$ add2virtualenv ..`

3. Install the requirements:  
   `$ pip install -r requirements.txt`

B. Create the Example Project

1. Create the Django Project:  
   `$ django-admin startproject django_photobooth_example`
   
2. Move manage.py to outside project's folder:  
   `$ cp django_photobooth_example/manage.py .`

2. Create Test App:  
   `$ python manage.py startapp test_app`

3. Add to INSTALLED_APPS in settings.py:  
 * django_extensions - For runserver_plus
 * photobooh_widget
 * test_app
 
4. Added FORM_RENDERER tp settings.py:  
 
       FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

4. Update the database:  
  `$ python manage.py migrate`

5.  To be able to use the, it needs to be in a HTTPS connection. Run the
    test server as this:  
    `$ python manage.py runserver_plus 9000 --cert-file cert.crt`

