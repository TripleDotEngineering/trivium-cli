################################################################################
#
# Makefile
#
# Copyright (c) 2021, Triple Dot Engineering LLC
#
# This file defines the build processes and common build-related commands for
# the Trivium CLI. Instructions for the use of these commands can be found
# in the project README file.
#
################################################################################
PYTHON = python3
SITE_PACKAGES=`$(PYTHON) -c "import site; print('\n'.join(site.getsitepackages()))"`

.PHONY: test clean
.SILENT: test clean

all: test

test:
	echo "+--------------------------------------------------------------------+"
	echo "|                                                                    |"
	echo "|  Trivium CLI Test Framework                                        |"
	echo "|                                                                    |"
	echo "|  Copyright (c) 2021, Triple Dot Engineering LLC                    |"
	echo "|                                                                    |"
	echo "+--------------------------------------------------------------------+"
	echo ""
	echo "Running tests ..."
	echo ""
	python3 -m unittest test.unit -q -c

lint:
	PYTHONPATH=. pylint trivium

install:
	$(PYTHON) setup.py install

clean:
	rm -rf  ./build
	rm -rf `find . -name "__pycache__"`
	rm -f `which trivium`
	for PKG in $(SITE_PACKAGES); do \
		rm -rf $$PKG/trivium; \
		rm -f $$PKG/trivium-*.egg-info; \
	done

