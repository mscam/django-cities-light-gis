from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cities_light_test',                      # Or path to database file if using sqlite3.
        'USER': 'cities_light_test',                      # Not used with sqlite3.
        'PASSWORD': 'test',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


