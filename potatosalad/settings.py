#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging


class Config(object):
    # Basic app settings
    ENV = None
    DEBUG = True
    TESTING = False

    # JSON config
    JSON_INDENT = 4
    JSON_SORT_KEYS = True

    # Security
    USE_SSL = False

    # Logging
    LOG_FORMAT = '%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s'
    LOG_DATE_FORMAT = '%m/%d/%Y %H:%M:%S'
    SQLALCHEMY_LOG_LEVEL = logging.WARNING
    DEFAULT_LOG_LEVEL = logging.DEBUG
    ERROR_404_HELP = False

    OPBEAT = {
        'ORGANIZATION_ID': os.getenv('OPBEAT_ORG_ID'),
        'APP_ID': os.getenv('OPBEAT_APP_ID'),
        'SECRET_TOKEN': os.getenv('OPBEAT_SECRET_TOKEN'),
        'INCLUDE_PATHS': ['potatosalad']
    }

    # CORS Settings
    REDIS_URL = 'redis://localhost/potatosalad'
    RATELIMIT_STORAGE_URL = REDIS_URL
    CORS_ALLOW_HEADERS = (
        'Content-Type',
        'Authorization',
        'Origin',
    )
    CORS_ORIGINS = ('*',)
    CORS_ALWAYS_SEND = True

    PROFILE = bool(os.environ.get('PROFILE', False))

    MAX_IMAGE_WIDTH = int(os.getenv('MAX_IMAGE_WIDTH', 3840))
    MAX_IMAGE_HEIGHT = int(os.getenv('MAX_IMAGE_HEIGHT', 2400))


class TestConfig(Config):
    # Basic app settings
    ENV = 'test'
    TESTING = True

    # Security
    SECRET_KEY = 'test'

    SQLALCHEMY_LOG_LEVEL = logging.WARNING


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
    CORS_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')

    # Logging configuration
    DEFAULT_LOG_LEVEL = logging.INFO

    # Celery backend configuration
    REDIS_URL = os.getenv('REDIS_URL', Config.REDIS_URL)
