#!/bin/bash
cat potatosalad/johncena.txt

gunicorn --config gunicorn.conf.py potatosalad:create_app\(\)
