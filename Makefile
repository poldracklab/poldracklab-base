test:
	python -m pytest tests
	python -m doctest src/poldracklab/*.py src/poldracklab/*/*.py

makedocs:
	pdoc --html -o docs src/poldracklab
