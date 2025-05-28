install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval data_science.ipynb

format:
	black *.py

all: install lint test format
