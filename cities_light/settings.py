"""
Settings for this application. The most important is TRANSLATION_LANGUAGES
because it's probably project specific.

.. py:data:: TRANSLATION_LANGUAGES

    List of language codes. It is used to generate the alternate_names property
    of cities_light models. You want to keep it as small as possible.
    By default, it includes the most popular languages according to wikipedia,
    which use a rather ascii-compatible alphabet. It also contains 'abbr' which
    stands for 'abbreviation', you might want to include this one as well.

    See:

     - http://download.geonames.org/export/dump/iso-languagecodes.txt

    Example::

        CITIES_LIGHT_TRANSLATION_LANGUAGES = ['es', 'en', 'fr', 'abbr']

.. py:data:: INCLUDE_COUNTRIES

    List of country codes to include. It's None by default which lets all
    countries in the database. But if you only wanted French and Belgium
    countries/regions/cities, you could set it as such::

        CITIES_LIGHT_INCLUDE_COUNTRIES = ['FR', 'BE']

.. py:data:: COUNTRY_SOURCES

    A list of urls to download country info from. Default is countryInfo.txt
    from geonames download server. Overridable in
    ``settings.CITIES_LIGHT_COUNTRY_SOURCES``.

.. py:data:: REGION_SOURCES

    A list of urls to download region info from. Default is
    admin1CodesASCII.txt from geonames download server. Overridable in
    ``settings.CITIES_LIGHT_REGION_SOURCES``.

.. py:data:: CITY_SOURCES

    A list of urls to download city info from. Default is cities15000.zip from
    geonames download server. Overridable in
    ``settings.CITIES_LIGHT_CITY_SOURCES``.

.. py:data:: TRANSLATION_SOURCES

    A list of urls to download alternate names info from. Default is
    alternateNames.zip from geonames download server. Overridable in
    ``settings.CITIES_LIGHT_TRANSLATION_SOURCES``.

.. py:data:: SOURCES

    A list with all sources, auto-generated.

.. py:data:: DATA_DIR

    Absolute path to download and extract data into. Default is
    cities_light/data. Overridable in ``settings.CITIES_LIGHT_DATA_DIR``

.. py:data:: INDEX_SEARCH_NAMES

    If your database engine for cities_light supports indexing TextFields (ie.
    it is **not** MySQL), then this should be set to True. You might have to
    override this setting with ``settings.CITIES_LIGHT_INDEX_SEARCH_NAMES`` if
    using several databases for your project.

.. py:data:: CITIES_LIGHT_APP_NAME

    Modify it only if you want to define your custom cities models, that
    are inherited from abstract models of this package.
    It must be equal to app name, where custom models are defined.
    For example, if they are in geo/models.py, then set
    ``settings.CITIES_LIGHT_APP_NAME = 'geo'``.
    Note: you can't define one custom model, you have to define all of
    cities_light models, even if you want to modify only one.
"""
from __future__ import unicode_literals

import os.path

from django.conf import settings

__all__ = ['COUNTRY_SOURCES', 'REGION_SOURCES', 'CITY_SOURCES',
    'TRANSLATION_LANGUAGES', 'TRANSLATION_SOURCES', 'SOURCES', 'DATA_DIR',
    'INDEX_SEARCH_NAMES', 'INCLUDE_COUNTRIES', 'DEFAULT_APP_NAME',
    'CITIES_LIGHT_APP_NAME']

COUNTRY_SOURCES = getattr(settings, 'CITIES_LIGHT_COUNTRY_SOURCES',
    ['http://download.geonames.org/export/dump/countryInfo.txt'])
REGION_SOURCES = getattr(settings, 'CITIES_LIGHT_REGION_SOURCES',
    ['http://download.geonames.org/export/dump/admin1CodesASCII.txt'])
CITY_SOURCES = getattr(settings, 'CITIES_LIGHT_CITY_SOURCES',
    ['http://download.geonames.org/export/dump/cities15000.zip'])
TRANSLATION_SOURCES = getattr(settings, 'CITIES_LIGHT_TRANSLATION_SOURCES',
    ['http://download.geonames.org/export/dump/alternateNames.zip'])
TRANSLATION_LANGUAGES = getattr(settings, 'CITIES_LIGHT_TRANSLATION_LANGUAGES',
    ['es', 'en', 'pt', 'de', 'pl', 'abbr'])

SOURCES = list(COUNTRY_SOURCES) + list(REGION_SOURCES) + list(CITY_SOURCES)
SOURCES += TRANSLATION_SOURCES

DATA_DIR = getattr(settings, 'CITIES_LIGHT_DATA_DIR',
    os.path.normpath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'data')))

INCLUDE_COUNTRIES = getattr(settings, 'CITIES_LIGHT_INCLUDE_COUNTRIES', None)

# MySQL doesn't support indexing TextFields
INDEX_SEARCH_NAMES = getattr(settings, 'CITIES_LIGHT_INDEX_SEARCH_NAMES', None)
if INDEX_SEARCH_NAMES is None:
    INDEX_SEARCH_NAMES = True
    for database in list(settings.DATABASES.values()):
        if 'mysql' in database['ENGINE'].lower():
            INDEX_SEARCH_NAMES = False

DEFAULT_APP_NAME = 'cities_light'
CITIES_LIGHT_APP_NAME = getattr(settings, 'CITIES_LIGHT_APP_NAME',
    DEFAULT_APP_NAME)
