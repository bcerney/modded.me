# django-playground

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

django-admin startproject dj_play
cd dj_play/
./manage.py startapp quotes_api

./manage.py makemigrations quotes_api
./manage.py migrate


>>> from quotes_api.serializers import QuoteSerializer
>>> serializer = QuoteSerializer()
>>> print(repr(serializer)
... )
QuoteSerializer():
    id = IntegerField(label='ID', read_only=True)
    text = CharField(style={'base_template': 'textarea.html'})
    author = CharField(allow_blank=True, max_length=200, required=False)
>>>


# docker
# https://docs.docker.com/compose/django/
docker build -t <tag> .


sudo docker-compose up -d --build

# https://docs.docker.com/compose/gettingstarted/
$ docker-compose up -d

Starting composetest_redis_1...
Starting composetest_web_1...

$ docker-compose ps

Name                 Command            State       Ports
-------------------------------------------------------------------
composetest_redis_1   /usr/local/bin/run         Up
composetest_web_1     /bin/sh -c python app.py   Up      5000->5000/tcp



# gitlab-ci

- psql config
# https://gitlab.com/gitlab-examples/postgres/-/blob/master/.gitlab-ci.yml




TODO:

- create psql db user best practices
- multi-env config for django/psql, env file or folder? best practices, both docker/django/psql
- update version pinning w/ pip-compile, automate via makefile: https://martin-thoma.com/python-requirements/
- makefile updates, .env for variables, any others from list: https://www.freecodecamp.org/news/django-project-best-practices-for-happy-developers/
- 3rd party packages: https://learndjango.com/tutorials/essential-django-3rd-party-packages
- gitlab-ci.yml

- integrate nginx, redis: https://realpython.com/django-development-with-docker-compose-and-machine/
- also: https://cloudonaut.io/how-to-dockerize-your-python-django-application-for-aws-fargate/

- add bootstrap navbar: https://pypi.org/project/django-bootstrap-navbar/
- create landing page w/ login link, index becomes user dashboard
- CRUD operations for quotes/reflections
- all-auth later on
- password reset: https://learndjango.com/tutorials/django-password-reset-tutorial



