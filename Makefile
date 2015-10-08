SHELL := /bin/bash

help:
	@echo 'Usage:'
	@echo '    make release -- build and release to PyPI'

release:
	python setup.py register sdist bdist_wheel upload
