# Django MangaLib

"Local MangaLib" website written in Django.

## Overview

This web application creates an online catalog for a small local manga library, where users can browse available titles and manage their accounts, leaving comments on titles.

The main features that have currently been implemented are:

* There are models for books, book copies, genre, language and authors, comments.
* Users can view list and detail information for titles and authors, search title and author by name.
* Admin users can create and manage models. The admin has been optimised.
* Librarians can renew reserved books, create, update, delete titles and authors.

![Home Page](https://raw.githubusercontent.com/mdluffy/django-mangalib/main/catalog/static/images/main.png)


## Quick Start

To get this project up and running locally on your computer:
1. Set up the Python development environment.
1. Assuming you have Python setup, run the following commands:
   ```
   pip install -r requirements.txt
   ./manage.py makemigrations
   ./manage.py migrate
   ./manage.py collectstatic
   ./manage.py test
   ./manage.py createsuperuser
   ./manage.py runserver

1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
