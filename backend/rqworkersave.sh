#!/bin/sh
start_rqworker () {
     python manage.py rqworker --pid rqworker_pid
}
start_rqworker & watchmedo shell-command \
    --patterns="*.py;*.txt" \
    --recursive \
    --command='pkill -2 $(cat rqworker_pid) &&  start_rqworker'
    .
