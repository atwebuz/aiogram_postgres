pip install python3.11
pipenv install python3.11
pip install django
pipenv install django
pipenv shell
python -m django --version
pip --freeze

django-admin startproject ebozor
cd ebozor
python manage.py startapp products

In the ebozor/settings.py change Installed_Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products' -> like this
]

## Run server 
```
python manage.py runserver 
```
