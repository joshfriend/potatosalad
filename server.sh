#!/bin/bash

# Let FLASK_SERVER variable choose which server is started
# http://stackoverflow.com/a/13946679/1255482

# https://devcenter.heroku.com/articles/optimizing-dyno-usage#python
WEB_CONCURRENCY=${WEB_CONCURRENCY:-3}
GUNICORN_TIMEOUT=${GUNICORN_TIMEOUT:-10}

# Restart workers if source changed
if [ "$GUNICORN_RELOAD" ]; then
    EXTRA_ARGS='--reload'
fi

cat potatosalad/johncena.txt

gunicorn potatosalad:create_app\(\) \
    -b 0.0.0.0:$PORT                \
    -w $WEB_CONCURRENCY             \
    -t $GUNICORN_TIMEOUT            \
    $EXTRA_ARGS
