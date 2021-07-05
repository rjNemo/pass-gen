.PHONY: lint
lint: 
	black -l 99 .
	flake8 .
	mypy . 
	vulture .
	bandit .

.PHONY: test
test: 
	pytest -v app/