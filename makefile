.PHONY: help run black flake test


help:
	@echo "run: run the project locally"
	@echo "black: format code"
	@echo "flake: lint the code"
	@echo "test: run the tests"
	@echo "format: format code with isort, black, pylint, flake8"

run:
	uvicorn src.app:app

black:
	black src

flake:
	flake8 src

test:
	pytest --cov --cov-config=.coveragerc --cov-report=html

format: black flake
