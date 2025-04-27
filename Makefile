lint:
	poetry run ruff format .
	poetry run black .
	flake8 --exclude .venv --ignore=E501,W503
	isort .