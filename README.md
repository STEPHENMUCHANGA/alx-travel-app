## alx-travel-app
### Django Project Setup with API Documentation and Database Configuration
### Objective: Set up the Django project with the necessary dependencies, configure the database, and add Swagger for API documentation.
```bash
setting up virtual environment
python3 -m venv env
source env/bin/activate

--- Install Django and dependencies pip install django djangorestframework django-cors-headers drf-yasg mysqlclient django-environ celery ---

--- requirements ---

```txt
Django>=4.2
djangorestframework
django-cors-headers
drf-yasg
mysqlclient
django-environ
celery
```
--- .env ---
 ```env
SECRET_KEY='your-secret-key'
DB_NAME='alx_db'
DB_USER='your_mysql_user'
DB_PASSWORD='your_mysql_password'
DB_HOST='localhost'
DB_PORT='3306'
```
--- settings.py ---
```python
import os
import environ
from pathlib import Path

# Env setup
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'listings',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

CORS_ALLOW_ALL_ORIGINS = True
```
--- urls.py ---

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="API documentation for ALX Travel App",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```
--- celery ---
```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```
--- listings---

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel App"})
```
--- urls.py ---

`listings/urls.py`
```python
from django.urls import path
from .views import HelloWorld

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello'),
]
```

--- running the app ---

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Swagger UI is available at: `http://localhost:8000/swagger/`

