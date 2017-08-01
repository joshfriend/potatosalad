#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from cStringIO import StringIO

import pytest
from mock import patch
from PIL import Image


def get_test_image(name):
    return Image.open(
        os.path.join(
            os.path.dirname(__file__),
            '../images/',
            name
        )
    )


def image_url(w, h, ext=None):
    url = '/%i/%i' % (w, h)
    if ext is not None:
        url += '.%s' % ext
    return url


class TestImageApi(object):
    def test_image_size_is_limited(self, app, client):
        with app.app_context():
            maxh = app.config['MAX_IMAGE_HEIGHT']
            maxw = app.config['MAX_IMAGE_WIDTH']

        r = client.get(image_url(maxw, maxh))
        assert r.status_code == 200

        r = client.get(image_url(maxw + 1, maxh))
        assert r.status_code == 400

        r = client.get(image_url(maxw, maxh + 1))
        assert r.status_code == 400

    @pytest.mark.parametrize('format,status', [
        ('jpg', 200),
        ('jpeg', 200),
        ('png', 200),
        ('bmp', 200),
        ('asdf', 400),
    ])
    def test_allows_formats(self, format, status, client):
        r = client.get(image_url(1, 1, format))
        assert r.status_code == status

    @patch('potatosalad.api.image.pick_random_image')
    def test_png_w_alpha_source_to_jpg_target(self, pick_image, client):
        pick_image.return_value = get_test_image('alpha.png')

        r = client.get(image_url(1, 1, 'jpg'))
        assert r.status_code == 200

    def default_format_is_jpg(self, client):
        r = client.get(image_url(1, 1))
        assert r.status_code == 200
        assert r.mimetype == 'image/jpeg'

    def test_get_iamge(self, client):
        dimensions = (100, 200)
        r = client.get(image_url(*dimensions))
        assert r.status_code == 200

        f = StringIO(r.get_data())
        img = Image.open(f)

        assert img.size == dimensions
