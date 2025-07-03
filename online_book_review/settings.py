########### Import necessary modules ###########
from pathlib import Path
import os

########### Build paths inside the project ###########
BASE_DIR = Path(__file__).resolve().parent.parent

########### Quick-start development settings (not for production) ###########
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

########### SECURITY WARNING: Keep the secret key secret in production ###########
SECRET_KEY = 'django-insecure-t^)ddpyz3xfkg*6v9pmf&!hl)07us-r#w0arieks_l&yg-_l%#'

########### SECURITY WARNING: Don't run with debug turned on in production! ###########
DEBUG = True

########### Define allowed hosts ###########
ALLOWED_HOSTS = []

########### Application definition ###########
INSTALLED_APPS = [
    'django.contrib.admin',  ########### Django admin panel ###########
    'django.contrib.auth',  ########### Authentication system ###########
    'django.contrib.contenttypes',  ########### Content types framework ###########
    'django.contrib.sessions',  ########### Session management ###########
    'django.contrib.messages',  ########### Messaging framework ###########
    'django.contrib.staticfiles',  ########### Static files handling ###########
    'accounts',  ########### Our custom accounts app ###########
    'books',  ########### Our custom books app ###########
]

########### Middleware configurations ###########
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

########### URL configuration ###########
ROOT_URLCONF = 'online_book_review.urls'

########### Templates settings ###########
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  ########### Templates directory ###########
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  ########### Request context ###########
                'django.contrib.auth.context_processors.auth',  ########### Authentication context ###########
                'django.contrib.messages.context_processors.messages',  ########### Messaging context ###########
            ],
        },
    },
]

########### WSGI application configuration ###########
WSGI_APPLICATION = 'online_book_review.wsgi.application'

########### Database configuration (SQLite used) ###########
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

########### Password validators ###########
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

########### Internationalization ###########
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

########### Static files (CSS, JavaScript, Images) ###########
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

########### Default primary key field type ###########
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

########### Media files configuration (for uploaded images like book covers) ###########
MEDIA_URL = '/media/'  ########### URL to access media files ###########
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  ########### Directory to store uploaded media files ###########
