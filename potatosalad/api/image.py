#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import mimetypes
from cStringIO import StringIO

from flask import send_file, current_app
from werkzeug.exceptions import BadRequest
from PIL import Image

from potatosalad.api import api
from potatosalad.util import cache_control, crop_resize


def _is_image(path):
    mime, _ = mimetypes.guess_type(path)
    return 'image' in str(mime)


# Load images in memory instead of constantly reading them from disk
IMAGE_DIR = os.path.abspath(os.path.dirname(__file__) + '../../../images')
IMAGE_FILES = filter(_is_image, os.listdir(IMAGE_DIR))
images = []
for path in IMAGE_FILES:
    path = os.path.join(IMAGE_DIR, path)
    images.append(Image.open(path))


ALLOWED_IMAGE_FORMATS = {
    'jpg': 'jpeg',  # Valid extension but not recognized by PIL
    'jpeg': 'jpeg',
    'bmp': 'bmp',
    'png': 'png',
}


def serve_pil_image(img, fmt):
    fmt = ALLOWED_IMAGE_FORMATS[fmt]
    mimetype = 'image/' + fmt
    f = StringIO()
    img.save(f, fmt, quality=70)
    f.seek(0)
    return send_file(f, mimetype=mimetype)


@api.route('/<int:w>/<int:h>.<ext>')
@api.route('/<int:w>/<int:h>')
@cache_control('max-age=60')
def placeholder_image(w, h, ext='jpeg'):
    # Check max dimensions
    maxh = current_app.config['MAX_IMAGE_HEIGHT']
    maxw = current_app.config['MAX_IMAGE_WIDTH']
    if h > maxh or w > maxw:
        raise BadRequest('Image must be smaller than %ix%i' % (maxw, maxh))

    if ext not in ALLOWED_IMAGE_FORMATS:
        raise BadRequest(
            'Allowed formats are: %s' % ', '.join(ALLOWED_IMAGE_FORMATS)
        )

    img = random.choice(images)
    img = crop_resize(img, (h, w))
    return serve_pil_image(img, ext)
