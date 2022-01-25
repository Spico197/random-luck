
all: format clean test_report build docs
	echo 'finished'

.PHONY: build
build: clean
	python3 setup.py sdist bdist_wheel

.PHONY: test_upload
test_upload:
	python3 -m twine upload --repository testpypi dist/*

.PHONY: upload
upload:
	python3 -m twine upload --repository pypi dist/*

.PHONY: docs
docs:
	cd docs && make clean
	cd docs && sphinx-apidoc -o . ../rex &&	make html

.PHONY: format
format:
	black .

.PHONY: test
test:
	pytest -vv .
	flake8

.PHONY: test_report
test_report:
	coverage run -m pytest -vv .
	coverage report -m
	flake8

.PHONY: clean
clean:
	cd docs && make clean
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -f .coverage
	rm -f coverage.xml
	find . | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf

.PHONY: serve_docs
serve_docs:
	python -m http.server --directory docs/_build/html
