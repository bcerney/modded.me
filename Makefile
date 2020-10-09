# https://www.freecodecamp.org/news/django-project-best-practices-for-happy-developers/

# TODO: any need to dynamically determine root?
DJ_ROOT=dj_play

.PHONY: install
install: ## Install requirements
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: migrate
migrate: ## Make and run migrations
	./$(DJ_ROOT)/manage.py makemigrations
	./$(DJ_ROOT)/manage.py migrate

.PHONY: runserver
runserver: migrate ## Run Django server
	./$(DJ_ROOT)/manage.py runserver 0.0.0.0:8000

.PHONY: test
test: ## Run tests
	./$(DJ_ROOT)/manage.py migrate
	./$(DJ_ROOT)/manage.py test

.PHONY: up
up: ## Run local server
	docker-compose up

.PHONY: build
build: ## Run local server
	docker-compose build

.PHONY: docker-run
docker-run: migrate runserver