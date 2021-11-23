# NOTICE:
# This file is intended for executing the project for development and Gitlab CI testing
# it is not intended to be used in Dockerfiles or deployment pipelines


ifneq ($(wildcard .env),)
	# load our .env
	include .env
	export
endif

VENV_DIR=_venv

# this is needed to make sure `make <command>` does not skip if we have a directory that matches the target name
.PHONY: all setup run test

.DEFAULT: help

clean:
	@rm -rf _venv test-output.log coverage .coverage

test-setup:
	@# remove old venv if it exists
	@if [ -d "${VENV_DIR}" ]; then \
		echo "removing existing virutal env found in ${VENV_DIR}/"; \
		rm -rf "${VENV_DIR}"; \
	fi

	@echo "creating new virtual env at ${VENV_DIR}/"
	@python3 -m venv ${VENV_DIR}
	@echo "installing test-requirements"
	@${VENV_DIR}/bin/pip3 install -qq --upgrade pip;
	@# ${VENV_DIR}/bin/pip3 install -U -v -r test-requirements.txt;
	@${VENV_DIR}/bin/pip3 install -U -e .[test-requirements];

setup:
	@# remove old venv if it exists
	@if [ -d "${VENV_DIR}" ]; then \
		echo "removing existing virutal env found in ${VENV_DIR}/"; \
		rm -rf "${VENV_DIR}"; \
	fi

	@echo "creating new virtual env at ${VENV_DIR}/"
	@python3 -m venv ${VENV_DIR}
	@echo "installing requirements"
	@${VENV_DIR}/bin/pip3 install -qq --upgrade pip;
	@# ${VENV_DIR}/bin/pip3 install -U -v -r requirements.txt;
	@${VENV_DIR}/bin/pip3 install -U -e .[requirements];

.enforce-setup: # checks if venv exists, or creates it and installs packages
	@if [ ! -d "${VENV_DIR}" ]; then \
		echo "venv missing, running setup"; \
		make setup; \
	fi

.enforce-test-setup: # checks if venv exists, or creates it and installs packages
	@if [ ! -d "${VENV_DIR}" ]; then \
		echo "venv missing, running setup"; \
		make test-setup; \
	fi

.check-env: # attempts to load .env file and then verifies for required env vars
	@. ci/check_env.sh

lint: .enforce-test-setup ## verifies that code complies with spec
	@${VENV_DIR}/bin/flake8 --ignore=E501 src

run: .enforce-setup .check-env  ## RELEASE=2021-summer make upload-project-release : uploads the notebook source to a databricks shared release location
	@if [ -z "${MODULE}" ]; then \
		echo "module variable not set.  use command MODULE='numbered_module' make run"; \
	else \
		echo "executing test rig ${MODULE}"; \
		${VENV_DIR}/bin/python3 -m src.gpio_test_rig ${MODULE}; \
	fi

build: .enforce-test-setup lint ## creates a binary distribution wheel for the library code
	@${VENV_DIR}/bin/python3 setup.py sdist; \
	echo "dist/`${VENV_DIR}/bin/python3 setup.py --fullname`.tar.gz"

test: .enforce-test-setup
	@./${VENV_DIR}/bin/flake8 --ignore=E501,N802,W504 src test
	@echo "running tests"
	./${VENV_DIR}/bin/pytest --cov=src test

test-single: .enforce-test-setup
	@./${VENV_DIR}/bin/flake8 --ignore=E501,N802,W504 src test
	@echo "running tests"
	@. ./run_tests.sh integration-single test_transform_stage.py no-kafka
