flake:
	python -m flake8 . --config=tox.ini

mypy:
	python -m mypy . --config-file mypy.ini
