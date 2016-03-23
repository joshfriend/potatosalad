# John Cena Placeholder Image Generator

[![Build Status][travis-badge]][travis-status]
[![Coverage Status][coveralls-badge]][coveralls-status]

## Instructions
Potatosalad works like most other placeholder image generator sites, like
[Place Harold][placeharold] or [Placekitten][placekitten]. Put the image width
and height (and optionally, a format) in the URL:

`https://potatosalad.herokuapp.com/<width>/<height>.<format>`

For example:

`https://potatosalad.herokuapp.com/320/240.jpg`

Would give you a picture like this:

![example](https://potatosalad.herokuapp.com/320/240.jpg)

### Supported Image Formats

The default format (if none is given) is `.jpg`, but the following are
supported:

* `jpg` and `jpeg`
* `png`
* `bmp`

## Requirements:

* [PyPy 5.0.1][pypy]
* [Virtualenv][virtualenv]

## Running Style Checkers
The following python checkers are available:

* `pep8`: [PEP8][pep8] style checker
* `pep257` [PEP257][pep257] docstring checker
* `flake8`: Combines PEP8 with [PyFlakes][pyflakes], a static analysis tool

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

[travis-badge]: http://img.shields.io/travis/joshfriend/potatosalad/master.svg
[travis-status]: https://travis-ci.org/joshfriend/potatosalad
[coveralls-status]: https://coveralls.io/r/joshfriend/potatosalad
[coveralls-badge]: http://img.shields.io/coveralls/joshfriend/potatosalad/master.svg
[placeharold]: http://placeharold.com/
[placekitten]: https://placekitten.com/
[pypy]: http://pypy.org/download.html
[virtualenv]: http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation
[pyflakes]: https://pypi.python.org/pypi/pyflakes
[pep8]: http://legacy.python.org/dev/peps/pep-0008/
[pep257]: http://legacy.python.org/dev/peps/pep-0257/
