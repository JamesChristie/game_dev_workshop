PYTHON=`which python`
NAME=`python setup.py --name`

all: init dev source

dev: check test

init:
	pip install -r requirements-dev.txt
	pip install -r requirements.txt

test:
	./pyspec.sh

ci-test:
	$(MAKE) check
	./pyspec.sh

source:
	$(PYTHON) setup.py sdist

check:
	find . -name \*.py | grep -v "tests/*test_*.py" | xargs pylint --errors-only --reports=n

clean:
	$(PYTHON) setup.py clean
	rm -rf build/ MANIFEST dist build libmorris.egg-info
	find . -name '*.pyc' -delete
