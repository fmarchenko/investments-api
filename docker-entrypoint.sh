#!/usr/bin/env bash

WORKDIR=/app
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

function run_api(){
    echo "Docker Entrypoint: Run api"
    python $WORKDIR/run_api.py
}

function run_migrations(){
    echo "Docker Entrypoint: Run migrations"
    alembic upgrade head
}

function run_devserver(){
    echo "Docker Entrypoint: Run DevServer"
    adev runserver $WORKDIR/run_api.py --app-factory make_app -p $API_PORT
}

case "$1" in
    "")
        run_migrations
        run_api
        ;;
    "run")
        run_migrations
        run_api
        ;;
    "run_api")
        run_api
        ;;
    "devserver")
        run_devserver
        ;;
    "migrate")
        run_migrations
        ;;
    *)
        echo "Unknown command '$1'. please use one of: [run, run_api, migrate, test, help]"
        exit 1
        ;;
esac
