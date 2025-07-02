## alx-travel-app
### Django Project Setup with API Documentation and Database Configuration
### Objective: Set up the Django project with the necessary dependencies, configure the database, and add Swagger for API documentation.
#### django>=4.2
#### djangorestframework
#### django-cors-headers
#### drf-yasg
#### mysqlclient
#### django-environ
#### celery

 settings.py 
#### import os
#### import environ
#### from pathlib import Path

# Initialise environment variables
#### env = environ.Env()
#### environ.Env.read_env()

#### BASE_DIR = Path(__file__).resolve().parent.parent

#### SECRET_KEY = env("SECRET_KEY")
#### DEBUG = True
#### ALLOWED_HOSTS = []

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

ROOT_URLCONF = 'alx_travel_app.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', default='3306'),
    }
}

CORS_ALLOW_ALL_ORIGINS = True

# ===================== urls.py (project-level) =====================
#### from django.contrib import admin
#### from django.urls import path, include
#### from rest_framework import permissions
#### from drf_yasg.views import get_schema_view
#### from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="API documentation for the ALX Travel App",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# ===================== .env (example) =====================
#### SECRET_KEY='your-secret-key'
#### DB_NAME='alx_db'
#### DB_USER='root'
#### DB_PASSWORD='password123'
#### DB_HOST='localhost'
#### DB_PORT='3306'

