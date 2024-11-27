from pathlib import Path
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-hbc&b3lbt54-4+yn6%dp5j$u)4+_yoxu-g9nzjx0dx=js89zq4'

DEBUG = False

ALLOWED_HOSTS = [
    '8000-davidkilty-portpro4sub-ap96dgcq6mc.ws.codeinstitute-ide.net',
    'itsgivingtips-abddf5f67e8a.herokuapp.com', 
    'localhost',
]
 
CSRF_TRUSTED_ORIGINS = [
    'https://8000-davidkilty-portpro4sub-ap96dgcq6mc.ws.codeinstitute-ide.net', 
    'https://itsgivingtips-abddf5f67e8a.herokuapp.com',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myproject.mainapp',
]
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]



ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='postgresql://uzgxsspspo2:bkFpIgNlH0Gb@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/igloo_hurt_nacho_787472')
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


STATICFILES_DIRS = [BASE_DIR / 'static']  
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if os.environ.get ('DISABLE_COLLECTSTATIC', None):
    STATICFILES_STORAGE = None

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'mainapp.User'

LOGIN_URL = '/logintipper/'
LOGIN_REDIRECT_URL = '/'
