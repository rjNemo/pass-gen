.PHONY: lint
lint: 
	pipenv run black -l 99 .
	pipenv run flake8 .
	pipenv run mypy . 
	pipenv run vulture .
	pipenv run bandit .

.PHONY: test
test: 
	pytest -v

.PHONY: cli
cli: 
	pipenv run python app/main.py

