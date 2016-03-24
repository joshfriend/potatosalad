#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging


class Config(object):
    # Basic app settings
    ENV = None
    DEBUG = True
    TESTING = False

    # Logging
    LOG_FORMAT = '%(name)-16s | %(levelname)-8s | %(message)s'
    DEFAULT_LOG_LEVEL = logging.DEBUG
    ERROR_404_HELP = False

    OPBEAT = {
        'ORGANIZATION_ID': os.getenv('OPBEAT_ORG_ID'),
        'APP_ID': os.getenv('OPBEAT_APP_ID'),
        'SECRET_TOKEN': os.getenv('OPBEAT_SECRET_TOKEN'),
        'INCLUDE_PATHS': ['potatosalad']
    }

    # CORS Settings
    CORS_ALLOW_HEADERS = (
        'Content-Type',
        'Origin',
    )
    CORS_ORIGINS = ('*',)
    CORS_ALWAYS_SEND = True

    PROFILE = bool(os.environ.get('PROFILE', False))

    MAX_IMAGE_WIDTH = int(os.getenv('MAX_IMAGE_WIDTH', 3840))
    MAX_IMAGE_HEIGHT = int(os.getenv('MAX_IMAGE_HEIGHT', 2400))

    ANALYTICS_TID = os.getenv('ANALYTICS_TID', 'test')


class TestConfig(Config):
    # Basic app settings
    ENV = 'test'
    TESTING = True


class DevConfig(Config):
    """Development configuration."""
    # Basic app settings
    ENV = 'dev'

    CORS_ORIGINS = (
        'http://localhost:5000',
    )


class ProdConfig(Config):
    """Staging configuration."""
    # Basic app settings
    ENV = 'production'
    DEBUG = False

    # CORS settings
    CORS_ORIGINS = os.getenv(
        'CORS_ALLOWED_ORIGINS',
        ','.join(Config.CORS_ORIGINS)
    ).split(',')

    # Logging configuration
    DEFAULT_LOG_LEVEL = logging.INFO
