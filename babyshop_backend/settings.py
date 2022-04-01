import os
from pathlib import Path

from django.core.checks import database


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#rc_v7+@s=*6qu*p2rnx&7-=zpdl$)yl@gl4#+g=ch&h^%fy*('

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # packages
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',

    # apps
    'shop'
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ]
}

# SOCIAL_AUTH_VK_OAUTH2_KEY = 'your app client id'
# SOCIAL_AUTH_VK_OAUTH2_SECRET = 'your app client secret'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1062528334768-q6eisv3hpa9e6gnbv4nefaoblrfjmanf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    
    'django.contrib.auth.backends.ModelBackend',
    
    # 'social_core.backends.vk.VKOAuth2',
    # 'social_core.backends.yandex.YandexOAuth2',
    # 'drf_social_oauth2.backends.DjangoOAuth2',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

LOGIN_REDIRECT_URL = '/products/products/1/'
LOGOUT_REDIRECT_URL = '/'

ROOT_URLCONF = 'babyshop_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'babyshop_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
