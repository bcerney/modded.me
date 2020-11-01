# https://www.freecodecamp.org/news/django-project-best-practices-for-happy-developers/

# TODO: any need to dynamically determine root?
DJ_ROOT=dj_play
EC2=ec2-3-237-9-28.compute-1.amazonaws.com
env=$(ENV)

.PHONY: push
push: ## Run force-push.sh
	./scripts/force-push.sh

.PHONY: compile
compile: ## Compile requirements
	pip install --upgrade pip
	pip-compile -U requirements.in

.PHONY: install-dev
install-dev: ## Install dev requirements
	pip install --upgrade pip
	pip install -r requirements-dev.in
	pip install -r requirements.txt

.PHONY: install
install: ## Install requirements
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: black
black: ## black formatter
	black .

# Django management

.PHONY: makemigrations
makemigrations: ## Make migrations
	./$(DJ_ROOT)/manage.py makemigrations

.PHONY: migrate
migrate: ## Run migrations
	./$(DJ_ROOT)/manage.py migrate

.PHONY: static
static: ## Make and run migrations
	./$(DJ_ROOT)/manage.py collectstatic

.PHONY: runserver
runserver: migrate ## Run Django server
	./$(DJ_ROOT)/manage.py runserver 0.0.0.0:80

.PHONY: gunicorn
gunicorn: migrate ## Run Django server
	cd $(DJ_ROOT) && gunicorn --bind 0.0.0.0:80 dj_play.wsgi:application

.PHONY: shell
shell: ## Run Django shell
	./$(DJ_ROOT)/manage.py shell_plus

.PHONY: test
test: migrate ## Run tests
	./$(DJ_ROOT)/manage.py test

# Docker

.PHONY: build
build: ## Run local server
	docker-compose -f docker-compose.$(env).yml build

.PHONY: up
up: ## Run local server
	docker-compose -f docker-compose.$(env).yml up

.PHONY: up-debug
up-debug: ## Run local server with Pdb debug access
	docker-compose -f docker-compose.dev.yml run --service-ports web

.PHONY: logs
logs: ## Run local server
	docker-compose -f docker-compose.$(env).yml logs

.PHONY: down
down: ## Run local server
	docker-compose -f docker-compose.$(env).yml down

.PHONY: exec
exec: ## Run local server
	docker-compose -f docker-compose.$(env).yml exec web bash

.PHONY: ssh-ec2-user
ssh-ec2-user: ## Run local server;TODO: parameterize
	ssh -i ~/.ssh/dj-play.pem ec2-user@$(EC2)

.PHONY: deploy-test
deploy-test: ## Fresh test deploy
	./scripts/aws-deploy-test.sh

.PHONY: deploy-snapshot-test
deploy-snapshot-test: ## Deploy using test-latest snapshot
	./scripts/aws-deploy-snapshot-test.sh

.PHONY: snapshot-test
snapshot-test: ## Create test-latest snapshot
	./scripts/create-snapshot-test.sh

.PHONY: deploy-prod
deploy-prod: ## Fresh prod deploy
	./scripts/aws-deploy-prod.sh

.PHONY: deploy-snapshot-prod
deploy-snapshot-prod: ## Deploy using prod snapshot
	./scripts/aws-deploy-snapshot-prod.sh

.PHONY: snapshot-prod
snapshot-prod: ## Create prod snapshot
	./scripts/create-snapshot-prod.sh
