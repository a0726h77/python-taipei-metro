all:
	@ echo '*** ***'

test:
	python -m unittest discover -v -s tests/ -p '*_test.py'
