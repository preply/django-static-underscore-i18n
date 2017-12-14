build:
	@python setup.py sdist
	@python setup.py bdist_wheel

upload: build
	@twine upload dist/*

test:
	@py.test -q tests || exit 1

lint:
	@flake8 src/staticunderscorei18n tests

coverage:
	@py.test -q tests --cov=src/staticunderscorei18n --cov-report=html || exit 1

clean:
	@rm -fr build dist

.PHONY: build upload test lint coverage clean
