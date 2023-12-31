import os
import dj_database_url

"""
Django settings for kunda project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uhv@%gzrp8h=6@!%ap=d)@&g(y1h*b_ix6tj(t%x*p)+kv*s1o'
SECRET_KEY = os.environ.get('SECRET_KEY', default='#*(#HD)%gzrp8h=6@!%ap=d)@&g(y1h*b_ix6tj(t%x*p)+kv*s1o')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Enable installed packages
    'whitenoise.runserver_nostatic',
    "auditlog",
    "rest_framework",
    "django.contrib.humanize",
    "axes",
    'django_filters',
    # 'corsheaders',
    # 'notifications',
    # Enable the kunda apps
    'stories.apps.StoriesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # "authentication.middleware.OneSessionPerUserMiddleware",
    # "core.middleware.HttpSecurityMiddleware",
    # "core.middleware.DisableHeadMethodMiddleware",
    # "core.middleware.DisableClientSideCachingMiddleware",
    # 'corsheaders.middleware.CorsMiddleware',
    # 'corsheaders.middleware.CorsPostCsrfMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'ratelimit.middleware.RatelimitMiddleware',
    'axes.middleware.AxesMiddleware',
    'axes.middleware.AxesStandaloneBackend',
]

ROOT_URLCONF = 'kunda.urls'

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

WSGI_APPLICATION = 'kunda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default_v2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default':
        dj_database_url.config(        
            # Feel free to alter this value to suit your needs.        
            default='postgresql://postgres:postgres@localhost:5432/mysite',        
            conn_max_age=600    
        )


}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

if not DEBUG:    
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = 'KundaKids <no-reply@kundakids.com>'

# LOGGING
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
    # 'filters': {
    #     'special': {
    #         '()': 'logging.SpecialFilter',
    #         'foo': 'bar',
    #     },
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    'handlers': {
        # 'console': {
        #     'level': 'INFO',
        #     'filters': ['require_debug_true'],
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'simple'
        # },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/app_django.logs',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'core.email_backend.EmailBackend',
            # 'filters': ['special'],
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            # 'handlers': ['console', 'file', 'mail_admins'],
            'handlers': ['file', 'mail_admins'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'core': {
            #'handlers': ['console', 'mail_admins'],
            'handlers': ['mail_admins'],
            'level': 'INFO',
            # 'filters': ['special'],
            'formatter': 'verbose'
        }
    }
}