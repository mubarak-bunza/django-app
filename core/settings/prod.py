from .base import * # noqa
import dj_database_url
from decouple import config

DEBUG = False
DATABASES = {
    'default': {
        **dj_database_url.parse(config('DATABASE_URL'), engine='django.db.backends.postgresql'),
        'ENGINE': 'django.db.backends.postgresql',
    }
}
