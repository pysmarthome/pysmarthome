clean:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +

release: dist
	twine upload dist/*

dist: clean
	python setup.py sdist
	ls -l dist

install: clean
	python setup.py install
