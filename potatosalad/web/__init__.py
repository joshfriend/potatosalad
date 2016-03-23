#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

site = Blueprint(
    'site',
    __name__,
    # map / url to _static/ folder
    static_folder='_static',
    static_url_path='',
    template_folder='_templates'
)


# Import the resources to add the routes to the blueprint before the app is
# initialized
from . import (  # NOQA
    index,
)
