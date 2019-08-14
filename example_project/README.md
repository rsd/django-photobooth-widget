Photobooth Widget Example Project
=================================

Test Photobooth
---------------
A. Prepare the environment.

1. Create the virtualenv:  
`$ virtualenv -p python3 venv`  
`$ source venv/bin/activate`

2. Add parent directory, for photobooth modules access:  
`'$  add2virtualenv ..'`

3. Install the requirements:  
`$ pip install -r requirements.txt`

B. Create the Example Project

1. Create the Django Project  
`$ django-admin startproject django_photobooth_example`

2. Add django_extensions to INSTALLED_APPS in settings.py.
This is needed for SSL test server.

3. Add photobooth_widget to the INSTALLED_APPS in settings.py.

4. Update the database:  
  `$ python django_photobooth_example/manage.py migrate`

5.  To be able to use the, it needs to be in a HTTPS connection. Run the
    test server as this:  
    `$ python django_photobooth_example/manage.py runserver_plus 9000
    --cert-file cert.crt`

