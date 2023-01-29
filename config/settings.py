from . import SETUP
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%673^1pu7ook&vhvgoo*l(#(ji!p+r424cvejsws%intfprglq'

DEBUG = bool(SETUP.DEBUG)

ALLOWED_HOSTS = ["*"]

# Celery settings
CELERYD_APPS = ['communicator_api.tasks.celery.CeleryAppConfig']
CELERYD__BEAT_APPS = ['communicator_api.tasks.celery.CeleryAppConfigBeat']
CELERY_BROKER_URL = SETUP.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = SETUP.CELERY_RESULT_BACKEND
REDIS_URL = SETUP.CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60

# Application definition

DJANGO_APPS = [
    'django.contrib.contenttypes',
    'django_filters'
]
THIRD_PARTY_APPS = [
    'rest_framework',
    # Health check
    'health_check',
    'health_check.db',
    'health_check.contrib.celery_ping',
    'health_check.contrib.redis',
]

LOCAL_APPS = [
    'communicator_api'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + CELERYD_APPS + CELERYD__BEAT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom
    'communicator_api.middleware.error_middleware.ErrorMiddleware', 
]
if SETUP.ENVIRONMENT in ['localhost']:
    MIDDLEWARE += ['communicator_api.middleware.sql_middleware.SqlPrintingMiddleware']


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'communicator',
        'USER': SETUP.POSTGRES_USER,
        'PASSWORD': SETUP.POSTGRES_PWD,
        'HOST': SETUP.POSTGRES_HOST,
        'PORT': SETUP.POSTGRES_PORT,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": SETUP.REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CLOSE_CONNECTION": True,
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        },
    }
}

REST_FRAMEWORK = {
    # "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    "UNAUTHENTICATED_USER": None,
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 30,
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

LANGUAGE_CODE = "es-CO"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = "config.asgi.communicator_api"
