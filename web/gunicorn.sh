#!/bin/sh
# This runs a gunicorn with using a config file `gunicron.conf.py`
cd ./web && gunicorn app:app