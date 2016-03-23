#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os.path
import logging

from flask import render_template

from potatosalad._info import ROOT, HOSTNAME
from potatosalad.web import site
from potatosalad.util import log
from potatosalad.util import cache_control

README_FILE = os.path.join(ROOT, 'README.md')
README = open(README_FILE, 'rb').read()

# Rewrite absolute URLS in images links to be relative
README = re.sub(r'\(https?:\/\/%s\/(.*)\)' % HOSTNAME, '(\\g<1>)', README)


@site.route("/")
@cache_control('max-age=86400')
def index():
    return render_template('index.html.j2', body=README)
