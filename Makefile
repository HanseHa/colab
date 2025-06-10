install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval data_science.ipynb
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py 

all: install test format lint
