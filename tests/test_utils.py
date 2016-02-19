#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mock import Mock
from PIL import Image

from potatosalad.util import crop_resize


class TestCropRezise(object):
    def test_resize_no_crop(self):
        image = Mock()
        image.crop.return_value = image
        image.size = (10, 10)

        target = (20, 20)
        crop_resize(image, target)

        assert image.crop.called is False
        image.resize.assert_called_with(target, Image.ANTIALIAS)

    def test_resize_vertical_crop(self):
        image = Mock()
        image.crop.return_value = image
        image.size = (10, 10)

        target = (5, 10)
        crop_resize(image, target)

        assert image.crop.called is True
        image.crop.assert_called_with((2, 0, 8, 10))
        image.resize.assert_called_with(target, Image.ANTIALIAS)

    def test_resize_horizontal_crop(self):
        image = Mock()
        image.crop.return_value = image
        image.size = (10, 10)

        target = (10, 5)
        crop_resize(image, target)

        assert image.crop.called is True
        image.crop.assert_called_with((0, 2, 10, 8))
        image.resize.assert_called_with(target, Image.ANTIALIAS)
