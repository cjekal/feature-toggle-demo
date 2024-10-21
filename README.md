# feature-toggle-demo

## Installation Steps
*These steps do not need to be repeated*

1. `brew install python3`
1. `python3 -m venv env`
1. `. env/bin/activate`
1. `pip install Django`
1. `pip install django_rest_framework`
1. `django-admin startproject mysite frontend`
1. `django-admin startproject project backends/payment_svc`
1. `django-admin startproject project backends/user_svc`
1. `cd backends/payment_svc/`
    1. update `settings.py` to include `rest_framework` in the `INSTALLED_APPS` global list
    1. `python manage.py startapp api`
    1. update `settings.py` to include `api` in the `INSTALLED_APPS` global list
1. `cd backends/user_svc/`
    1. update `settings.py` to include `rest_framework` in the `INSTALLED_APPS` global list
    1. `python manage.py startapp api`
    1. update `settings.py` to include `api` in the `INSTALLED_APPS` global list
1. `docker-compose build && docker-compose up`
1. log into unleash
    1. go to http://localhost:4242 and login with `admin`/`unleash4all` - these are the default credentials
