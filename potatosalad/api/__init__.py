#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from functools import wraps
from time import time

from flask import Blueprint, g, request, current_app

log = logging.getLogger(__name__)

endpoints = Blueprint('endpoints', __name__)


def if_debug(func):
    @wraps(func)
    def wrapper(response):  # pragma: no cover
        if current_app.debug:
            return func(response)
        return response
    return wrapper


@endpoints.before_request
def record_request_start_time():
    if current_app.debug:  # pragma: no branch
        g._request_start_time = time()


@endpoints.after_request
@if_debug
def log_request(response):
    """Log any requests/responses with an error code"""
    duration = (time() - g._request_start_time) * 1000
    path = request.path.encode('utf-8')
    log.debug('%7s: %s - %i (%.1lfms)', request.method, path,
              response.status_code, duration)
    return response


# Import the resources to add the routes to the blueprint before the app is
# initialized
from . import (  # NOQA
    image,
)
