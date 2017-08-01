#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cStringIO import StringIO

from flask import send_file, current_app
from werkzeug.exceptions import BadRequest

from potatosalad.api import endpoints
from potatosalad.util import (
    pick_random_image,
    remove_transparency,
    cache_control,
    crop_resize,
)


ALLOWED_IMAGE_FORMATS = {
    'jpg': 'jpeg',  # Valid extension but not recognized by PIL
    'jpeg': 'jpeg',
    'bmp': 'bmp',
    'png': 'png',
}

#: Formats which support alpha channel
_ALPHA_FORMATS = [
    'png',
]


def serve_pil_image(img, fmt):
    fmt = ALLOWED_IMAGE_FORMATS[fmt]
    mimetype = 'image/' + fmt

    # Replace transparency with white if not supported by target format
    if img.mode in ('RGBA', 'LA') and fmt not in _ALPHA_FORMATS:
        img = remove_transparency(img)

    f = StringIO()
    img.save(f, fmt, quality=70)
    f.seek(0)
    return send_file(f, mimetype=mimetype)


@endpoints.route('/<int:w>/<int:h>.<ext>')
@endpoints.route('/<int:w>/<int:h>')
@cache_control('max-age=60')
def placeholder_image(w, h, ext='jpg'):
    # Check max dimensions
    maxh = current_app.config['MAX_IMAGE_HEIGHT']
    maxw = current_app.config['MAX_IMAGE_WIDTH']
    if h > maxh or w > maxw:
        raise BadRequest('Image must be smaller than %ix%i' % (maxw, maxh))

    if ext not in ALLOWED_IMAGE_FORMATS:
        raise BadRequest(
            'Allowed formats are: %s' % ', '.join(ALLOWED_IMAGE_FORMATS)
        )

    img = pick_random_image()
    img = crop_resize(img, (w, h))
    return serve_pil_image(img, ext)
