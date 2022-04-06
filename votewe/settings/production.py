from votewe.settings.base import *
import os, dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

MIDDLEWARE.insert(2, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES['default'] = dj_database_url.parse(
    url=os.getenv('DATABASE_URL'), conn_max_age=600
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')

STATIC_DIRS = Path.cwd().joinpath(BASE_DIR).joinpath('votewe/assets')
STATICFILES_DIRS = [
    STATIC_DIRS,
]

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')