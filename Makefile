all:
	@ echo '*** ***'

install-dependencies:
	@ sudo pip install -r requirements.txt

test:
	python -m unittest discover -v -s tests/ -p '*_test.py'
