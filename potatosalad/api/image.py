#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import mimetypes
from cStringIO import StringIO

from flask import jsonify, send_file
from PIL import Image

from potatosalad.api import api, log


def _is_image(path):
    mime, _ = mimetypes.guess_type(path)
    return 'image' in str(mime)


IMAGE_DIR = os.path.abspath(os.path.dirname(__file__) + '../../../images')
IMAGES = filter(_is_image, os.listdir(IMAGE_DIR))


def serve_pil_image(img):
    f = StringIO()
    img.save(f, 'JPEG', quality=70)
    f.seek(0)
    return send_file(f, mimetype='image/jpeg')


def center_crop(img, target):
    ch, cw = map(float, img.size)
    current_ratio = cw / ch
    tw, th = map(float, target)
    target_ratio = tw / th
    log.debug("Crop aspect %.3f -> %.3f", current_ratio, target_ratio)
    return img


def resize(img, target):
    ch, cw = img.size
    tw, th = target
    log.debug('Resize %ix%i -> %ix%i', ch, cw, th, tw)
    return img


@api.route('/<int:h>/<int:w>')
def placeholder_image(h, w):
    path = os.path.join(IMAGE_DIR, random.choice(IMAGES))
    img = Image.open(path)
    img = center_crop(img, (h, w))
    img = resize(img, (h, w))
    return serve_pil_image(img)
