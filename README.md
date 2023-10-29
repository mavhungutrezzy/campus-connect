# Campus Connect (1.0.0)
[![Tests](https://github.com/mavhungutrezzy/campus-connect/actions/workflows/django.yml/badge.svg)](https://github.com/mavhungutrezzy/campus-connect/actions/workflows/django.yml)
[![Django](https://img.shields.io/badge/Django-5.1.2-brightgreen)](href="https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org)
[![Django Rest Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.14-orange)](https://www.djangoproject.com/)


The 'Campus Connect' API is a comprehensive system designed to facilitate interactions between students, universities, and bursary providers. It leverages the power of Django REST framework and employs JWT (JSON Web Tokens) for secure authentication. The API provides several features to serve students, including bursaries management, application tracking for bursaries and courses, courses and university information, etc.

## 📖 API Documentation

The API documentation is available to help you understand how to use the 'Campus Connect' API. You can access the API documentation by visiting the following URL:

[API Documentation](https://campusconnect-yph529vr.b4a.run/api/v1/docs/)


## 📖 Installation

This project can be installed via Pip or Docker. To get started, clone the repository to your local computer and navigate to the project directory.

```shell
$ git clone https://github.com/yourusername/yourrepository.git
$ cd yourrepository
```

### Pip

Create a virtual environment, activate it, install the project requirements, perform database migrations, create a superuser, and run the development server.

```shell
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Access the site at http://127.0.0.1:8000
```

### Docker

If you prefer using Docker with PostgreSQL as the database, update the `DATABASES` section in the `django_project/settings.py` file to match the following configuration:

```python
# django_project/settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default PostgreSQL port
    }
}
```

Update the `INTERNAL_IPS` configuration in `django_project/settings.py` as well:

```python
# config/settings.py
# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
```

Build the Docker image, run the container, and execute the standard commands within Docker:

```shell
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
# Access the site at http://127.0.0.1:8000
```


## 🧪 Testing

We use both pytest and Django unittests for testing the 'Campus Connect' API.

### Running pytest

You can run pytest to execute the project's tests by using the following command:

```shell
(.venv) $ pytest
```

### Running Django unittests with Coverage

To run Django unittests with coverage, use the following command:

```shell
(.venv) $ coverage run manage.py test
```

You can then view the coverage report using:

```shell
(.venv) $ coverage report
```

For a more detailed HTML report, use:

```shell
(.venv) $ coverage html
```
