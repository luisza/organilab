# organilab
Simple laboratory organizer with multiples features:

- Laboratory builder and elegant presentation 
- Multi-laboratory management
- Reservation system
- Solution Calculator
- Procedures management
- Object limit notifications
- Internationalization

# Documentation

Documentation will be available in [read the docs](http://organilab.readthedocs.io/en/latest/)

# Installation 

Clone this repository 

	$ git clone git@github.com:solvo/organilab.git
	$ cd organilab

Create a virtualenv

	$ mkdir -p ~/entornos/
	$ virtualenv -p python3 ~/entornos/organilab
	$ source ~/entornos/organilab/bin/activate

Install requirements 

	$ pip install -r requirements.txt
	
# Run in development

Check your database configuration and sync your models

	$ python manage.py migrate

Create a superuser for admin views

	$ python manage.py createsuperuser

Run your development server

	$ python manage.py runserver
	
## happy hacking	

	
