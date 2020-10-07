# https://www.freecodecamp.org/news/django-project-best-practices-for-happy-developers/

DJ_ROOT=dj_play

.PHONY: install
install: ## Install requirements
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: migrate
migrate: ## Make and run migrations
	# TODO: fix this, wasn't creating quotes_app migrations
	./$(DJ_ROOT)/manage.py makemigrations
	./$(DJ_ROOT)/manage.py migrate

.PHONY: runserver
runserver: migrate ## Run Django server
	./$(DJ_ROOT)/manage.py runserver 0.0.0.0:8000

.PHONY: test
test: ## Make and run migrations
	# TODO: fix this, wasn't creating quotes_app migrations
	# ./$(DJ_ROOT)/manage.py makemigrations
	./$(DJ_ROOT)/manage.py test

.PHONY: up
up: ## Run local server
	docker-compose up

.PHONY: build
build: ## Run local server
	docker-compose build

.PHONY: docker-run
docker-run: migrate runserver
