from django.contrib.auth.models import User
from rest_framework import serializers

from quotes_app.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'owner']


class UserSerializer(serializers.ModelSerializer):
    quotes = serializers.PrimaryKeyRelatedField(many=True, queryset=Quote.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'quotes']