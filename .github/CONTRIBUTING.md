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
You run a development server as follows:

    $ make serve

By default, port 5000 is used unless the `$PORT` environment variable is set.

The virtualenv will be created automatically with the required dependencies. If
the requirements file (`requirements/dev.txt`) changes, running any command will
automatically cause the dependencies in the virtualenv to be updated.

Compiled python files and pytest cache files can be cleaned with:

    $ make clean

If you need to rebuild the virtualenv from scratch:

    $ make clean-all

## Pull Requests
Basic requirements for pull requests are as follows:

1. Write tests for new features or bugfixes and make sure the build passes on
   [Travis CI][travis-prs].
2. Check for missing code coverage. This is reported to the console whenever
   you run tests and is also shown on [Coveralls][coveralls-status].
3. Code should pass the `pep8` linter check.

[travis-prs]: https://travis-ci.org/joshfriend/potatosalad/pull_requests
[coveralls-status]: https://coveralls.io/r/joshfriend/potatosalad
[placeharold]: http://placeharold.com/
[placekitten]: https://placekitten.com/
[pypy]: http://pypy.org/download.html
[virtualenv]: http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation
[pyflakes]: https://pypi.org/project/pyflakes
[pep8]: http://legacy.python.org/dev/peps/pep-0008/
[pep257]: http://legacy.python.org/dev/peps/pep-0257/
