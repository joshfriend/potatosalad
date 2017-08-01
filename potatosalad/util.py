#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import logging
import functools
import mimetypes

from flask import make_response
from PIL import Image

from potatosalad._info import IMAGE_DIR

log = logging.getLogger(__name__)


def _is_image(path):
    mime, _ = mimetypes.guess_type(path)
    return 'image' in str(mime)


# Load images in memory instead of constantly reading them from disk
_IMAGE_FILES = filter(_is_image, os.listdir(IMAGE_DIR))
_images = []
for path in _IMAGE_FILES:
    path = os.path.join(IMAGE_DIR, path)
    _images.append(Image.open(path))


def pick_random_image():
    index = random.randint(0, len(_images) - 1)
    log.debug('Random image: %s', _IMAGE_FILES[index])
    return _images[index]


def remove_transparency(image):
    bg = Image.new(image.mode[:-1], image.size, '#ffffff')
    bg.paste(image, image.split()[-1])
    return bg


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
        img = img.crop(bounds)

    log.debug('Resize %ix%i -> %ix%i', ch, cw, th, tw)

    return img.resize(size, Image.ANTIALIAS)
