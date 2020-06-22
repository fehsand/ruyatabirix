import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#------------------------------------------------------------------------------
# local de açık yayında kapalı
SECRET_KEY = 'kg1!kr3a4h_*_79*p=p&_lht6&-u111u6uo=79g*8dqv3@ej!*'
# local de kapalı yayında açık olacak
#with open('/home/ruyatabirix/sc_ky.txt') as f:
#    SECRET_KEY = f.read().strip()


#--------------------------------------------------------------------------------
# local de açık yayında kapalı
DEBUG = True
# local de kapalı yayında açık olacak
#DEBUG = False
#--------------------------------------------------------------------------------


ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com', '.ruyatabirix.com',]

#--------------------------------------------------------------------------------
INSTALLED_APPS = [
    'ruyatabirleri.apps.RuyatabirleriConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'register',
    'django.contrib.sitemaps',
]
#-----------------------------------------------------------

#localde açık yayında kapalı
SITE_ID = 1
#yayında açık localde kapalı
#SITE_ID = 2

#---------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#----------------------------------------------------------

# local de açık yayında kapalı
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# yayında açık localde kapalı
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

#SECURE_HSTS_SECONDS = 60
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True
#SECURE_SSL_REDIRECT = True

#----------------------------------------------------------------

ROOT_URLCONF = 'ruyatabirix.urls'

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

WSGI_APPLICATION = 'ruyatabirix.wsgi.application'

#-----------------------------------------------------------------

#local de açık yayında kapalı
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ruyatabirix',
        'USER': 'root',
        'PASSWORD': 'Tgbyhn123+',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#yayında açık local de kapalı

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'ruyatabirix$ruyatabirix',
#        'USER': 'ruyatabirix',
#        'PASSWORD': 'Rfvtgb123+',
#        'HOST': 'ruyatabirix.mysql.pythonanywhere-services.com',
#    }
#}

#--------------------------------------------------------------------------

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'tr'

LANGUAGES = [('tr', _('Turkish')), ('en', _('English')),]

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join (BASE_DIR, 'locale'), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

