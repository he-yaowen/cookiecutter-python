.PHONY: init
init:
	@poetry install
	@poetry run pre-commit install

.PHONY: test
test:
	@poetry run pytest

.PHONY: coverage
coverage:
	@poetry run coverage run -m pytest
	@poetry run coverage report -m

.PHONY: lint
lint:
	@poetry run pylint src
