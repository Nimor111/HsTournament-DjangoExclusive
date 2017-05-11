import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tournament',
        'USER': 'tournamentuser',
        'PASSWORD': 'tournamentpass',
        'HOST': 'localhost',
        'TEST': {
            'NAME': 'test_hearthofstone',
            'USER': 'tournamentuser',
        },
        'PORT': '',
    }
}

DEBUG = True
