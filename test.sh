#!/usr/bin/env bash
set -x
set -e

DB=${DB:-postgresql}

function do_db() {
    python test_project/manage.py syncdb --traceback --noinput --settings=test_project.$1
    python test_project/manage.py migrate --noinput --traceback --settings=test_project.$1
    python test_project/manage.py cities_light --force-import-all --traceback --settings=test_project.$1
}

pip install -I -r test_project/requirements_south.txt

if [[ $DB = 'postgresql' ]]; then
    pip install psycopg2
    do_db settings_postgres
fi 

if [[ $DB = 'sqlite' ]]; then
    rm -rf test_project/db.sqlite
    do_db settings
fi
