#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from urllib import urlencode

import pytest
from flask.testing import FlaskClient

from potatosalad import create_app
from potatosalad.settings import TestConfig


class LoggingTestClient(FlaskClient):
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)

    def open(self, path, query=None, **kwargs):
        # Format querystring
        if query:
            path += '?{}'
            path = path.format(urlencode(query))

        # Debug printing
        r = super(self.__class__, self).open(path, **kwargs)
        self.log.debug('Response status: %i', r.status_code)
        self.log.debug('Response headers: \n%s', r.headers)
        if 'image' in r.mimetype:
            self.log.debug('Response data: <Binary Image Data>')
        else:
            self.log.debug('Response data: \n%s', r.get_data())

        return r


@pytest.yield_fixture(scope='module')
def app():
    yield create_app(TestConfig)


@pytest.yield_fixture(scope='module')
def client(app):
    app.test_client_class = LoggingTestClient
    yield app.test_client()
