lint:
	@ echo "🧹 sort imports…"
	@ poetry run isort .
	@ echo "💅 formatting…"
	@ poetry run black .
	@ echo "📏 linting…"
	@ poetry run flake8 .
	@ echo "☑️ type checking…"
	@ poetry run mypy .
	@ echo "⛑ safety check…"
	@ poetry run bandit -r --exclude=test .

test:
	@ echo "🧪 running tests…"
	@ poetry run pytest -v --cov=. --cov-report=html

cli:
	@ echo "🚀 running app…"
	@ poetry run python -m app

help:
	poetry run python -m app --help

.PHONY: test
