#!/usr/bin/env make

PYTHON = py
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
	coverage report --include="src/bin/*" -m

pylint:
	pylint *.py

flake8:
	flake8

pdoc:
	del doc\pdoc
	pdoc --html -o doc/pdoc .

pyreverse:
	del doc\uml
	rmdir doc\uml
	md doc\uml
	xcopy index.html doc\uml
	pyreverse src/ test/
	dot -Tpng classes.dot -o doc/uml/class_diagram.png
	dot -Tpng packages.dot -o doc/uml/packages_war.png
	del classes.dot
	del packages.dot
	ls -l doc/uml

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
