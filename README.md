# django-playground

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

django-admin startproject dj_play
cd dj_play/
./manage.py startapp quotes_app

./manage.py makemigrations quotes_app
./manage.py migrate


>>> from quotes_app.serializers import QuoteSerializer
>>> serializer = QuoteSerializer()
>>> print(repr(serializer)
... )
QuoteSerializer():
    id = IntegerField(label='ID', read_only=True)
    text = CharField(style={'base_template': 'textarea.html'})
    author = CharField(allow_blank=True, max_length=200, required=False)
>>> 