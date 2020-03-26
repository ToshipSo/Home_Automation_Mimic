# Tech-Stack
* Python 3.5 or above
* Django 3
* Django-rest-framework
* HTML, CSS, Javascript
* SQLite3

# Installation
* `pip install -r requirements.txt` to install python libraries.
* `python manage.py migrate` to migrate database.
* `python manage.py createsuperuser` and fill the form to create a user.

# Run Application
* `python manage.py runserver` to run application.
* Visit [http://localhost:8000](http://localhost:8000) to use app.
* Log in using your superuser credentials.
* Visit [http://localhost:8000/admin](http://localhost:8000/admin) to access django admin panel.

# Database
SQLite3 database is used in this project because it is default database in django.
SQLite3 databases can be easily managed in development environment and can be automatically migrated to PostgreSQL during 
deployment on Heroku or similar web-hosting services.

# Workflow
* User has to login first.
* After logging in user will be redirected to rooms page where user can view and add rooms.
* After entering in room user can add, view, delete and control smart devices.
* Each device is associated to a room. 
