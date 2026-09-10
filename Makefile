.PHONY: install migrate seed run test build clean docker-build docker-run

PYTHON ?= python
PIP ?= pip

install:
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) manage.py migrate

seed:
	$(PYTHON) manage.py seed_civiclaw_data

run:
	$(PYTHON) main.py runserver 0.0.0.0:8000

test:
	$(PYTHON) manage.py test tests

check:
	$(PYTHON) manage.py check

build:
	$(PYTHON) manage.py collectstatic --noinput

docker-build:
	docker build -t civiclaw:latest .

docker-run:
	docker run -p 8000:8000 civiclaw:latest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
