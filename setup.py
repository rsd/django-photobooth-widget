from setuptools import setup, find_packages
import os

VERSION = (0, 1, 1)
__version__ = '.'.join(map(str, VERSION))

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='django-photobooth-widget',
    version=__version__,
    description="A widget based on photobooth.js to take photos from the user's device camera.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Raul Dias",
    author_email="raul@dias.com.br",
    url="https://github.com/rsd/django-photobooth-widget.git",
    license="MIT",
    platforms=["any"],
    #packages=find_packages(exclude=("example_project", ".gitignore", "cert.crt", "cert.key")),
    packages=["django_photobooth_widget"],
    keywords='django-photobooth-widget',
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Operating System :: OS Independent",
    ],
)

