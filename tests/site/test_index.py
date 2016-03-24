#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestIndex(object):
    def test_favicon(self, client):
        r = client.get('/favicon.ico')
        assert r.status_code == 200

    def test_has_index_page(self, client):
        r = client.get('/')
        assert r.status_code == 200
        assert r.mimetype == 'text/html'
