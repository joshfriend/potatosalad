#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_cors import CORS
from flask_misaka import Misaka
from opbeat.contrib.flask import Opbeat

cors = CORS()
md = Misaka()
opbeat = Opbeat()
