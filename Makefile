PIP=`which pip`
PYTHON=`which python3`
NAME=`python setup.py --name`

all: init dev source

dev: check test

init:
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -r requirements.txt

test:
	./pyspec.sh

ci-test:
	$(MAKE) strict-lint
	./pyspec.sh

source:
	$(PYTHON) setup.py sdist

lint:
	find . -name \*.py | grep -v "tests/*test_*.py" | xargs pylint --errors-only --reports=n

strict-lint:
	find . -name \*.py | grep -v "tests/*test_*.py" | xargs pylint --reports=n

clean:
	$(PYTHON) setup.py clean
	rm -rf build/ MANIFEST dist build libmorris.egg-info
	find . -name '*.pyc' -delete
