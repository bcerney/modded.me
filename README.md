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
- create GitlabCI IAM user with reduced permissions
- Review gitlabci config options: https://docs.gitlab.com/ee/ci/yaml/README.html#include
- Resolve get-parameter usage in shell script: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters.html