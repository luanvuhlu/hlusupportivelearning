"""
Django settings for hlusupportivelearning project.

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
SECRET_KEY = ')w0+)e1po+*%sm3o4+o!y^k2_g9bdb9@r@^5*#wvln6qo&!9-o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
PROJECT_DIR=os.path.dirname(__file__)

# Application definition

INSTALLED_APPS = (
    # 'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'notification',
    'ckeditor',
    'treemenus',
    'easy_thumbnails',
    'dajaxice',
    'account',
    'document',
    'filemanager',
    'group',
    'news',
    'student',
    'tag',
    'timetable',
    'topic',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'hlusupportivelearning.urls'

WSGI_APPLICATION = 'hlusupportivelearning.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# settings.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'hlu',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'vi-Vi'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Add new lines
AUTH_USER_MODEL = 'account.CUser'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'dajaxice.finders.DajaxiceFinder',
)
TEMPLATE_CONTEXT_PROCESSORS =(
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

STATIC_ROOT= os.path.join(PROJECT_DIR,'static_media/')
STATICFILES_DIRS = ( os.path.join(PROJECT_DIR,'static/'),)
GRAPPELLI_ADMIN_TITLE="HLU"
GRAPPELLI_SWITCH_USER=True
GRAPPELLI_CLEAN_INPUT_TYPES=True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'hlu.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'account': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'group': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'news': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'student': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'topic': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates').replace('\\','/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

INTERNAL_IPS='127.0.0.1'
DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"
CKEDITOR_SLUGIFY_FILENAME=False
CKEDITOR_RESTRICT_BY_USER=True
CKEDITOR_JQUERY_URL='http://hlu.vn:8000/static/grappelli/jquery/jquery-1.9.1.min.js'
CKEDITOR_CONFIGS = {
    'default':{

    },
    'client-header': {
        'uiColor' : '#9AB8F3',
        'height': 200,
        'width': 500,
        'removeDialogTabs':'link:upload;image:Upload',
    },
    'client-content': {
        'uiColor' : '#9AB8F3',
        'height': 500,
        'width': 700,
        'removeDialogTabs':'link:upload;image:Upload',
    },
}
SELECT2_BOOTSTRAP=True
AUTO_RENDER_SELECT2_STATICS=False


MEDIA_ROOT= os.path.join(PROJECT_DIR,'media/')
MEDIA_URL='/media/'
