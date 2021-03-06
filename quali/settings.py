# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

SETTINGS_DIR=os.path.join(PROJECT_PATH,'settings.py')
STATICFILES_DIRS = os.path.join(PROJECT_PATH,'hewa/static'),
    

PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
# DATABASE_PATH = os.path.join(PROJECT_PATH, 'qh.db')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w^q$-=%@bx)454te%upk6!0vn1$q^ank$e))3hl($*2uy9uo#s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

INSTALLED_APPS = (
    # 'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    # 'contrib.staticfiles',
    'django.contrib.sites',

    'hewa',
    
    'django_tables2',
    # 'tastypie',
    'selectable',
    'selectable_select2',
    'south', #For managing changes to your database tables via data migrations.
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

ROOT_URLCONF = 'quali.urls'

WSGI_APPLICATION = 'quali.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    
)   
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'look-at-localsettings.py',
        'PASSWORD': "change-password-at-localsettings",
        'USER': 'root',
        'PORT': '3306',
        'HOST': '127.0.0.1' # 127.0.0.1
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
# MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'


# this is where the magic happens
try:
    import sys
    if os.environ.has_key('LOCAL_SETTINGS'):
        # the LOCAL_SETTINGS environment variable is used by the build server
        sys.path.insert(0, os.path.dirname(os.environ['LOCAL_SETTINGS']))
        from settings_test import *
    else:
        from localsettings import *
except ImportError:
    pass