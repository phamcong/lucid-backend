# LUCID BACKEND

## How to install

### [Lucid query interface (frontend: AngularJS 1)](https://github.com/phamcong/lucid-query-interface)

### PostgreSQL (backend: Django REST Framework)

+ Clone the git project: `git clone https://github.com/phamcong/lucid-backend.git`
+ Move into project folder: `cd lucid-backend`
+ Make sure that [python 3](https://www.python.org/downloads/), [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) are installed.
+ Create a new virtualenv: `virtualenv env` (on MacOs)
+ Activate virtual environment: `source env/bin/activate` (on MacOs)
+ Install requirements: pip intall -r requirements.txt
+ Move into backend folder: `cd lucicBackend`
+ Migrate database: `python manage.py migrate`
+ Create super user: `python manage.py createsuperuser`
+ Run server at post 8080: `python manage.py runserver 8080`