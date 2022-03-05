"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

#import django
#django.setup()

from pathlib import Path
import os


from django.urls import reverse



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = []


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b2-3my&u*^ii=h3fosbt)=uaxrvcjl4s!48m=412ul^nihc12&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'social_django',
    'images',
    'sorl.thumbnail',
    'actions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates')),
                 os.path.join(BASE_DIR, 'account', 'templates', 'images'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'




# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#VENV_PATH = os.path.dirname(BASE_DIR)
#STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')


STATIC_PATH = os.path.join('static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#LOGIN_REDIRECT_URL = reverse('dashboard')
#LOGIN_URL = reverse('login')
#LOGOUT_URL = reverse('logout')

LOGIN_REDIRECT_URL = '/account/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'prabhatwebcrone@gmail.com'
EMAIL_HOST_PASSWORD = 'Prabhat@123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'account.authentication.EmailAuthBackend',
#'social_auth.backends.facebook.FacebookBackend',
'social_core.backends.facebook.FacebookOAuth2',
'social.backends.twitter.TwitterOAuth',
)


SOCIAL_AUTH_FACEBOOK_KEY = '637630670837500' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '49e12b92ca1d6ba7aa34c4ca528114b8' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'hnpR3oD5ns1ozE3K2HzJ86vxn' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 'XpM0XGn2zroXUITBitcOZJOnzv34uDXcbLsf6neTNeSVTxnB89' # Twitter Consumer Secret

ABSOLUTE_URL_OVERRIDES = {
'auth.user': lambda u: reverse('user_detail',args=[u.username])
}