#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask.ext.cors import CORS
from opbeat.contrib.flask import Opbeat

cors = CORS()
opbeat = Opbeat()
