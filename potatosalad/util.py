#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import functools

from flask import make_response
from PIL import Image

log = logging.getLogger('api')


def cache_control(*directives):
    """Insert a Cache-Control header with the given directives."""
    def decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            # invoke the wrapped function
            rv = f(*args, **kwargs)

            # convert the returned value to a response object
            rv = make_response(rv)

            # insert the Cache-Control header and return response
            rv.headers['Cache-Control'] = ', '.join(directives)
            return rv
        return wrapped
    return decorator


def crop_resize(img, size):
    """Resize
    """
    ch, cw = img.size
    th, tw = size

    current_ar = ch / float(cw)
    target_ar = th / float(tw)

    log.debug("Crop aspect %.3f -> %.3f", target_ar, current_ar)

    bounds = None
    if current_ar > target_ar:
        # Crop horizontally
        xoffset = int((ch - target_ar * cw) / 2)
        bounds = (xoffset, 0, ch - xoffset, cw)
    elif current_ar < target_ar:
        # Crop vertically
        yoffset = int((cw - ch / target_ar) / 2)
        bounds = (0, yoffset, ch, cw - yoffset)

    if bounds:
        log.debug('Crop bounds: %s', bounds)
        img = img.crop(bounds)

    log.debug('Resize %ix%i -> %ix%i', ch, cw, th, tw)

    return img.resize(size, Image.ANTIALIAS)
