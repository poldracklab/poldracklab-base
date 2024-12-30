test:
	python -m pytest tests
	python -m doctest src/poldracklab/*.py src/poldracklab/*/*.py

build-docs:
	- rm -rf docs
	pdoc --html -o docs src/poldracklab
	git add docs
	git commit -m "Update documentation"
	