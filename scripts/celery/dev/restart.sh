#!/bin/bash

LOGS_DIR=$PROJECT_APP_DIR/var/logs
RUN_DIR=$PROJECT_APP_DIR/var/run

echo "-> Restarting celery workers"
. $PROJECT_APP_VENV/bin/activate
cd $PROJECT_APP_DIR
python manage.py celeryd_multi restart w1 \
    --pidfile=$RUN_DIR/%n.pid \
    --logfile=$LOGS_DIR/%n.log \
    --loglevel=INFO \
    -E
