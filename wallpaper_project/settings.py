import os
from pathlib import Path

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'tu_clave_secreta'

# Debug
DEBUG = True

# Allowed Hosts
ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wallpapers',  # Asegúrate de incluir tu aplicación aquí
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL de la raíz
ROOT_URLCONF = 'wallpaper_project.urls'

# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Base de datos (localhost)
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'wallpaper_db',
#        'USER': 'postgres',
#        'PASSWORD': 'root',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

# Base de datos (Docker)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wallpaper_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Archivos estáticos y medios
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Donde se recopilarán los archivos estáticos en producción

STATICFILES_DIRS = [

    BASE_DIR / 'static',  # Carpeta donde puedes colocar archivos estáticos adicionales

]