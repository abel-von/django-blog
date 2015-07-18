"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v)4xd!$2bqu&i-thh9$@_38oz$k_16(3-gmq*rnp-h%^9xo*0t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'blog'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


if 'SERVER_SOFTWARE' in os.environ:
  from sae.const import (
    MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
  )
else:
  # Make `python manage.py syncdb` works happy!
  MYSQL_HOST = 'localhost'
  MYSQL_PORT = '3306'
  MYSQL_USER = 'root'
  MYSQL_PASS = '20044002'
  MYSQL_DB  = 'bzblog'

DATABASES = {
  'default': {
    'ENGINE':  'django.db.backends.mysql',
    'NAME':  MYSQL_DB,
    'USER':  MYSQL_USER,
    'PASSWORD': MYSQL_PASS,
    'HOST':  MYSQL_HOST,
    'PORT':  MYSQL_PORT,
  }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/' 

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT= os.path.join(PROJECT_PATH,'..','media')

TEMPLATE_DIRS = (
 os.path.join(BASE_DIR, "templates/"),
)

