.PHONY: lint
lint: 
	pipenv run black -l 99 .
	pipenv run flake8 .
	pipenv run mypy . 
	# pipenv run vulture .
	pipenv run bandit -r --exclude=test .

.PHONY: test
test: 
	pipenv run pytest -v --cov=. --cov-report=html

.PHONY: cli
cli: 
	pipenv run python -m app

.PHONY: help
help: 
	pipenv run python -m app --help
