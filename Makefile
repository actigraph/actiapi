DUMMY: lint test format checks

lint:
	flake8 actiapi tests
	mypy actiapi
	pydocstyle actiapi
format:
	isort .
	black .
test:
	pytest
checks: format lint test
