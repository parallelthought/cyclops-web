"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from datetime import timedelta

dir_path=os.path.join(os.path.dirname( __file__ ), '..',)
config = {}
execfile(dir_path+"/config.conf", config) 

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))+'/database'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%q(qy(y#t7zo*_)tm#x0=o8m11_^eh_-n)%i8h^^wh%j&8s-8&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = config["DEBUG"]

GLOBAL_SETTINGS = {
       'PRO_DEBUG':True,
}

#PRO_DEBUG==True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    BASE_DIR +'/templates',
)


# Application definition

INSTALLED_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_menu',
    'south',


    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'web_ui.urls'

WSGI_APPLICATION = 'web_ui.wsgi.application'

LOGIN_REDIRECT_URL='/index/'
#LOGIN_URL='/accounts/login/?next=/demo/'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   # 'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}, 
             
    'default':{
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'db_cyclops',
        'USER': config["USER"],
        'PASSWORD': config["PASSWORD"],
        'HOST': config["HOST"],   # Or an IP Address that your DB is hosted on
        'PORT': config["PORT_DB"],
        'OPTIONS': {
                    "init_command": "SET foreign_key_checks = 0;",
                    },
    }
}

SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 6400 #age is in seconds=>2hours

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = ( 
    BASE_DIR +'/static',  
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


