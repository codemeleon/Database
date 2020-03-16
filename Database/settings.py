"""
Django settings for Database project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'anmolyouareanidiot'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# For neo4J database connections
#  NEOMODEL_NEO4J_BOLT_URL = os.environ.get(
#      'NEO4J_BOLT_URL', 'bolt://neo4j:anmol@localhost:7687')
#  NEOMODEL_SIGNALS = True
#  NEOMODEL_FORCE_TIMEZONE = False
#  NEOMODEL_ENCRYPTED_CONNECTION = True
#  NEOMODEL_MAX_POOL_SIZE = 50
# Application definition

# For future test purpose https://grappelliproject.com/

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'grappelli',
    #  'bootstrap_admin', # always before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    #  'django_neomodel',
    'MicroBiome',
    'leaflet',
    'djgeojson',
    'django_nvd3',
    'bootstrap4',
    'crispy_forms',
    'tags_input',
    'django_tables2',
    "taggit",
    #  'djide',
    #  'rooms',
]

TAGGIT_CASE_INSENSITIVE = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# For cached sesson management [Anmol]
SESSION_ENGINE = "django.contrib.sessions.backends.cache"


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]


ROOT_URLCONF = 'Database.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # 'html', added by Anmol #os.path.abspath("../html")
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

WSGI_APPLICATION = 'Database.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# GRAPPELLI_ADMIN_TITLE
GRAPPELLI_ADMIN_TITLE = "MicroBiome Admin Site"
GRAPPELLI_SWITCH_USER = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# os.path.abspath("static")  # added by Anmol
CRISPY_TEMPLATE_PACK = 'bootstrap4'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
# print(BASE_DIR)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    # "/home/devil/Documents/Tools/Database/staticfiles"
]


RESULTS_PER_PAGE = 50
