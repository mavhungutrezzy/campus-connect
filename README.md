# Campus Connect (1.0.0)

<table>
  <tr>
    <td>
      <a href="https://github.com/mavhungutrezzy/campus-connect/actions/workflows/django.yml">
        <img src="https://github.com/mavhungutrezzy/campus-connect/actions/workflows/django.yml/badge.svg" alt="Django Tests">
      </a>
    </td>
    <td>
      <a href="https://www.djangoproject.com/">
        <img src="https://img.shields.io/badge/Django-5.1.2-brightgreen" alt="Django Version">
      </a>
    </td>
    <td>
      <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python Version">
      </a>
    </td>
    <td>
      <a href="https://www.django-rest-framework.org/">
        <img src="https://img.shields.io/badge/Django%20REST%20Framework-3.12.4-orange" alt="Django REST Framework">
      </a>
    </td>
    <td>
      <a href="https://jwt.io/">
        <img src="https://img.shields.io/badge/JWT-JSON%20Web%20Tokens-9cf" alt="JWT">
      </a>
    </td>
  </tr>
</table>

The 'Campus Connect' API is a comprehensive system designed to facilitate interactions between students, universities, and bursary providers. It leverages the power of Django REST framework and employs JWT (JSON Web Tokens) for secure authentication. The API provides several features to serve students, including bursaries management, application tracking for bursaries and courses, courses and university information, etc.

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
