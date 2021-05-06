#!/usr/bin/env make

PYTHON = python
.PHONY: pydoc

all:

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@echo "Now activate the Python virtual environment:\n. .venv/bin/activate"
	@echo "Type 'deactivate' to deactivate."

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-all: clean clean-doc
	rm -rf .venv

unittest:
	 $(PYTHON) -m unittest discover . "*_test.py"

coverage:
	coverage run -m unittest discover . "*_test.py"
	coverage html
	coverage report -m

pylint:
	pylint *.py

flake8:
	flake8

pydoc:
	install -d doc/pydoc
	pydoc -w $(PWD)
	mv *.html doc/pydoc

pdoc:
	rm -rf doc/pdoc
	pdoc --html -o doc/pdoc .

doc: pdoc #pydoc sphinx

pyreverse:
	install -d doc/pyreverse
	pyreverse $(PWD)
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot
	ls -l doc/pyreverse

radon-cc:
	radon cc . -a

radon-mi:
	radon mi .

radon-raw:
	radon raw .

radon-hal:
	radon hal .

bandit:
	bandit -r .

lint: flake8 pylint

test: lint coverage
