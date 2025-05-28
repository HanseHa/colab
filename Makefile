install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval data_science.ipynb

format:
	black *.py

lint:
	pylint --disable=R,C

all: install lint test format
