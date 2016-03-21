# John Cena Placeholder Image Generator

[![Build Status](http://img.shields.io/travis/joshfriend/potatosalad/master.svg)](https://travis-ci.org/joshfriend/potatosalad)
[![Coverage Status](http://img.shields.io/coveralls/joshfriend/potatosalad/master.svg)](https://coveralls.io/r/joshfriend/potatosalad)

## Requirements:

* [PyPy 4.0.0](http://pypy.org/download.html)
* [Virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation)

## Running Style Checkers
The following python checkers are available:

* `pep8`: [PEP8](http://legacy.python.org/dev/peps/pep-0008/) style checker
* `pep257` [PEP257](http://legacy.python.org/dev/peps/pep-0257/) docstring checker
* `flake8`: Combines PEP8 with [PyFlakes](https://pypi.python.org/pypi/pyflakes), a static analysis tool

To run all checkers required to pass a build:

    $ make check

To run a specific check:

    $ make <checker-name>

## Development
You can then run a development server as follows:

    $ make serve

By default, port 5000 is used unless the `$PORT` environment variable is set.

The virtualenv will be created automatically with the required dependencies. If
the requirements file (`requirements/dev.txt`) changes, running any command will
automatically cause the dependencies in the virtualenv to be updated.

Compiled python files and pytest cache files can be cleaned with:

    $ make clean

If you need to rebuild the virtualenv from scratch:

    $ make clean-all

