# Project settings
PROJECT := PotatoSalad
PACKAGE := potatosalad
SOURCES := Makefile $(shell find $(PACKAGE) -name '*.py')
REQUIREMENTS_DEV := requirements/dev.txt
REQUIREMENTS_PROD := requirements/prod.txt

SYS_PYTHON := pypy
SYS_VIRTUALENV := virtualenv

# virtualenv paths (automatically detected from the system Python)
ENV := env
BIN := $(ENV)/bin
OPEN := open

# virtualenv executables
ifndef TRAVIS
	BIN_ := $(BIN)/
endif
PYTHON := $(BIN_)python
PIP := $(BIN_)pip
PEP8 := $(BIN_)pep8
FLAKE8 := $(BIN_)flake8
PEP257 := $(BIN_)pep257
PYTEST := $(BIN_)py.test
COVERAGE := $(BIN_)coverage
ACTIVATE := $(BIN_)activate
HONCHO := . $(ACTIVATE); $(BIN_)honcho

# Flags for PHONY targets
DEPENDS_DEV := $(ENV)/.depends-dev
ALL := $(ENV)/.all

# Main Targets ###############################################################

.PHONY: all
all: test check

.PHONY: ci
ci: flake8 test

# Development Installation ###################################################

.PHONY: env
env: .virtualenv

.PHONY: .virtualenv
.virtualenv: $(PIP)
$(PIP):
	$(SYS_VIRTUALENV) --python $(SYS_PYTHON) $(ENV)

.PHONY: depends
depends: .depends-dev

.PHONY: .depends-dev
.depends-dev: env Makefile $(DEPENDS_DEV)
$(DEPENDS_DEV): $(REQUIREMENTS_DEV) $(REQUIREMENTS_PROD)
	. $(ACTIVATE); \
	$(PIP) install --upgrade -r $(REQUIREMENTS_DEV)
	touch $(DEPENDS_DEV) # flag to indicate dependencies are installed

# Static Analysis ############################################################

.PHONY: check
check: flake8

.PHONY: flake8
flake8: depends
	$(FLAKE8) $(PACKAGE) tests

.PHONY: pep257
pep257: depends
	$(PEP257) $(PACKAGE)

# Testing ####################################################################

PYTEST_OPTS := --cov $(PACKAGE)  \
			   --cov-report html \
			   --cov-report term-missing

.PHONY: test
test: depends
	$(PYTEST) $(PYTEST_OPTS) tests

.PHONY: htmlcov
htmlcov:
	open htmlcov/index.html

# Development server #########################################################

.PHONY: serve
serve: depends
	GUNICORN_RELOAD=true $(HONCHO) start web -e .env

# Cleanup ####################################################################

.PHONY: clean
clean: .clean-dist .clean-test .clean-build
	rm -rf $(ALL)

.PHONY: clean-all
clean-all: clean .clean-env

.PHONY: .clean-env
.clean-env:
	rm -rf $(ENV)

.PHONY: .clean-build
.clean-build:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: .clean-test
.clean-test:
	rm -rf .coverage
	rm -f clover.xml coverage.xml
	rm -rf htmlcov

.PHONY: .clean-dist
.clean-dist:
	rm -rf dist build

