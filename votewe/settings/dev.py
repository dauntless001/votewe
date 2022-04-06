from votewe.settings.base import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!$_@np-)yoes7p-cx(rqes00ski-dr@95vcohwr-kqx709+(*)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'votwe.db',
}
# DATABASES['default'] = dj_database_url.parse(
#     url=os.getenv('DATABASE_URL'), conn_max_age=600
# )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')

STATIC_DIRS = Path.cwd().joinpath(BASE_DIR).joinpath('votewe/assets')
STATICFILES_DIRS = [
    
]

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')