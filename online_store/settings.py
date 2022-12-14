import os.path
import sys
from pathlib import Path

from django.utils.translation import gettext_lazy as _

from config import DATABASE_PASSWORD
from config import EMAIL_HOST_PASSWORD
from config import EMAIL_HOST_USER
from config import SECRET_KEY
from config import SERVER_EMAIL

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SECRET_KEY

DEBUG = True

ALLOWED_HOSTS = ['multishop.pp.ua', 'www.multishop.pp.ua', '127.0.0.1', 'testserver']

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'favorite',
    'basket',
    'users',
    'orders',
    'news',
    'ckeditor',
    'mptt',
    'nested_admin',
    'captcha',
    'debug_toolbar',
    'rest_framework',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'online_store.middleware.SessionAuthenticationMiddleware',
    'online_store.middleware.ExceptionLoggingMiddleware'
]

ROOT_URLCONF = 'online_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'basket.context_processors.basket_products_context',
                'favorite.context_processors.favorite_products_context',
                'users.context_processors.get_newsletter_subscription_form_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_store.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rocky0u0_django3',
        'USER': 'rocky0u0_django3',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': "rocky0u0.beget.tech",
        'PORT': '3306',
        'ATOMIC_REQUEST': False,
    },
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_data',
        'ATOMIC_REQUESTS': False,
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

AUTH_USER_MODEL = "users.User"

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('uk', _('Ukraine')),
)

TIME_ZONE = 'EET'

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
if DEBUG:
    STATIC_ROOT = ''
    STATICFILES_DIRS = (os.path.join('static'),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ['127.0.0.1']

CKEDITOR_UPLOAD_PATH = "uploads/"

LOGIN_URL = 'login'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
        'TIMEOUT': 120,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ukr.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
SERVER_EMAIL = SERVER_EMAIL
ADMINS = [
    ('Rocky', 'rocky01396@gmail.com'),
    ('Frank', "rocky113@ukr.net"),
]

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

CAPTCHA_FONT_SIZE = 40
CAPTCHA_IMAGE_SIZE = (120, 50)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

LOG_ROOT = os.path.join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_ROOT + '/logs.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
        },
        'root': {
            'handlers': ['mail_admins', 'console', 'file'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
