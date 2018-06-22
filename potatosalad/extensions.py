#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_cors import CORS
from flask_misaka import Misaka

cors = CORS()
md = Misaka()
