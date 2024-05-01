flake:
	python -m flake8 . --config=tox.ini

flake_toml:
	python -m flake8 . --toml-config=pyproject.toml

mypy:
	python -m mypy . --config-file pyproject.toml
