import os

INSTALLED_APPS = [
    'cacheops',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'tests',
]

ROOT_URLCONF = 'tests.urls'

MIDDLEWARE_CLASSES = []

AUTH_PROFILE_MODULE = 'tests.UserProfile'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Django replaces this, but it still wants it. *shrugs*
DATABASE_ENGINE = 'django.db.backends.sqlite3',
if os.environ.get('CACHEOPS_DB') == 'postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'cacheops',
            'USER': 'cacheops',
            'PASSWORD': '',
            'HOST': ''
        },
        'slave': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'cacheops_slave',
            'USER': 'cacheops',
            'PASSWORD': '',
            'HOST': ''
        },
    }
elif os.environ.get('CACHEOPS_DB') == 'postgis':
    POSTGIS_VERSION = (2, 1, 1)
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'cacheops',
            'USER': 'cacheops',
            'PASSWORD': '',
            'HOST': '',
        },
        'slave': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'cacheops_slave',
            'USER': 'cacheops',
            'PASSWORD': '',
            'HOST': '',
        },
    }
elif os.environ.get('CACHEOPS_DB') == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cacheops',
            'USER': 'cacheops',
            'PASSWORD': '',
            'HOST': '',
        },
        'slave': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cacheops_slave',
            'USER': 'cacheops',
            'PASSWORD': '',
            'HOST': '',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'sqlite.db',
            # Make in memory sqlite test db to work with threads
            # See https://code.djangoproject.com/ticket/12118
            'TEST': {
                'NAME': ':memory:cache=shared'
            }
        },
        'slave': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'sqlite_slave.db',
        }
    }


CACHEOPS_REDIS = {
    'startup_nodes': 'localhost:6379',
    # lazy starting redis client
    'skip_full_coverage_check': True,
    'init_slot_cache': False
}


def handle_timeout_error(e, *args, **kwargs):
    print(e, *args, **kwargs)
    


CACHEOPS_CLUSTER_ENABLED = True
CACHEOPS_REDIS_CONNECTION_TIMEOUT = 1
CACHEOPS_TIMEOUT_HANDLER = handle_timeout_error
CACHEOPS_DEFAULTS = {
    'timeout': 60*60
}
CACHEOPS = {
    'tests.local': {'local_get': True},
    'tests.cacheonsavemodel': {'cache_on_save': True},
    'tests.dbbinded': {'db_agnostic': False},
    'tests.*': {},
    'tests.noncachedvideoproxy': None,
    'tests.noncachedmedia': None,
    'auth.*': {},
}

if os.environ.get('CACHEOPS_PREFIX'):
    CACHEOPS_PREFIX = lambda q: 'p:'

CACHEOPS_LRU = bool(os.environ.get('CACHEOPS_LRU'))
CACHEOPS_DEGRADE_ON_FAILURE = bool(os.environ.get('CACHEOPS_DEGRADE_ON_FAILURE'))
ALLOWED_HOSTS = ['testserver']

SECRET_KEY = 'abc'

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'}]
