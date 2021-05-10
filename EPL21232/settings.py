"""
Django settings for EPL21232 project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR.joinpath("EPL21232")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "6cz0w7$4ee&dw%%(yjr=%&@=hdv%--fm-p7k=9bb=wg0xdw22("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "tfe-verbois-duprez.info.ucl.ac.be",
    "130.104.229.16",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "EPL21232.apps.accounts",
    "EPL21232.apps.contact",
    "EPL21232.apps.data",
    "EPL21232.apps.maps",
    'import_export',
]

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    #"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "EPL21232.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "EPL21232.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default="")
POSTGRES_DB = os.environ.get('POSTGRES_DB', default="")
POSTGRES_USER = os.environ.get('POSTGRES_USER', default="")
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default="")

# "ENGINE": "django.contrib.gis.db.backends.postgis",
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#ADMIN_LANGUAGE_CODE="fr-fr"
LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "public:index"
LOGOUT_REDIRECT_URL = "public:index"

# EMAIL SETTINGS => SendGrid as SMTP 
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_API_KEY = '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'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "nicolas.verbois@student.uclouvain.be"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'api_key'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY #api_key
EMAIL_PORT = 587
EMAIL_USE_TLS = True

IMPORT_EXPORT_USE_TRANSACTIONS = True

JET_DEFAULT_THEME = 'default'

JET_SIDE_MENU_COMPACT = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000