# https://www.freecodecamp.org/news/django-project-best-practices-for-happy-developers/

# TODO: any need to dynamically determine root?
DJ_ROOT=dj_play
EC2=ec2-3-236-15-76.compute-1.amazonaws.com
env=$(ENV)

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


.PHONY: build
build: ## Run local server
	docker-compose -f docker-compose.$(env).yml build

.PHONY: up
up: ## Run local server
	docker-compose -f docker-compose.$(env).yml up

.PHONY: up
down: ## Run local server
	docker-compose -f docker-compose.$(env).yml down

.PHONY: up
exec: ## Run local server
	docker-compose -f docker-compose.$(env).yml exec web bash

.PHONY: ssh-ec2-user
ssh-ec2-user: ## Run local server;TODO: parameterize
	ssh -i ~/.ssh/dj-play.pem ec2-user@$(EC2)

# TODO: add make snapshot-test, make snapshot-prod