#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


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

    def default_format_is_jpg(self, client):
        r = client.get(image_url(1, 1))
        assert r.status_code == 200

        assert r.headers['Content-Type'] == 'image/jpeg'
