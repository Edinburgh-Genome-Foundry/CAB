#!/bin/bash

python manage.py test --noinput 2> /var/log/test.log 1> /dev/null

if [ $? -ne 0 ]; then
    cat /var/log/test.log
    exit 1
fi

echo 'All tests successful.'
exit 0
