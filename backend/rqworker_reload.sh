#!/bin/sh
./rqworker_start.sh & watchmedo shell-command \
    --patterns="*.py;*.txt" \
    --recursive \
    --command='kill -2 $(cat rqworker_pid) ; ./rqworker_start.sh'
    .
