from django.contrib.auth.models import User
from rest_framework import serializers
from taggit_serializer.serializers import (TaggitSerializer,
                                           TagListSerializerField)

from quotes_app.models import Quote


class QuoteSerializer(serializers.ModelSerializer, TaggitSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tags = TagListSerializerField()

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'owner', 'tags']


class UserSerializer(serializers.ModelSerializer):
    quotes = serializers.PrimaryKeyRelatedField(many=True, queryset=Quote.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'quotes']
