#!/usr/bin/env python

'''The app module, containing the app factory function.'''

import os
import logging

from flask import Flask

from potatosalad.settings import DevConfig, ProdConfig
from potatosalad.extensions import (
    cors,
    opbeat,
)
from potatosalad.api import api, log as _api_log


FLASK_ENV = os.environ.get("FLASK_ENV")
if FLASK_ENV == 'production':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig


def create_app(config_object=DefaultConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    if not app.debug:
        opbeat.init_app(app)
    configure_logging(app)
    register_extensions(app)
    register_blueprints(app)
    install_middleware(app)
    _api_log.info("Serving up some delicious potato salad...")
    return app


def register_extensions(app):
    cors.init_app(app)


def register_blueprints(app):
    app.register_blueprint(api)


def configure_logging(app):
    log_levels = {
        'error': logging.ERROR,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG,
    }
    default_level = app.config['DEFAULT_LOG_LEVEL']
    level = log_levels.get(os.getenv('LOG_LEVEL'), default_level)
    logging.basicConfig(format=app.config['LOG_FORMAT'],
                        datefmt=app.config['LOG_DATE_FORMAT'])

    _api_log.setLevel(level)

    _cors_log = logging.getLogger('Flask-Cors')
    _cors_log.setLevel(logging.WARNING)

    _args_log = logging.getLogger('webargs.flaskparser')
    _args_log.setLevel(logging.WARNING)

    # Api does its own request logging
    _werkzeug_log = logging.getLogger('werkzeug')
    _werkzeug_log.setLevel(logging.ERROR)

    _sqla_log = logging.getLogger('sqlalchemy.engine')
    _sqla_log.setLevel(app.config['SQLALCHEMY_LOG_LEVEL'])


def install_middleware(app):  # pragma: no cover, manual test
    if bool(app.config.get('PROFILE', False)):
        from werkzeug.contrib.profiler import ProfilerMiddleware
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[10])
