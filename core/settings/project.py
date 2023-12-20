INSTALLED_APPS += [
    'rest_framework',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = +[
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.str('PG_DATABASE', default='postgres'),
            'USER': env.str('PG_USER', default='postgres'),
            'PASSWORD': env.str('PG_PASSWORD', default='postgres'),
            'HOST': env.str('DB_HOST', default='localhost'),
            'PORT': env.str('DB_PORT', default='5432'),
        },
    }

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
