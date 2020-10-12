.PHONY: migrate
migrate: ## Make and run migrations
	./manage.py makemigrations
	./manage.py migrate

.PHONY: gunicorn
gunicorn: migrate ## Run local server
	gunicorn dj_play.wsgi:application --bind 0.0.0.0:8000 --workers=4