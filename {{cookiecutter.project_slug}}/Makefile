.PHONY: init
init:
	@poetry install

.PHONY: test
test:
	@poetry run pytest

.PHONY: coverage
coverage:
	@poetry run coverage run -m pytest
	@poetry run coverage report -m
