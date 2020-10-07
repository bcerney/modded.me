from django.contrib.auth.models import User
from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from quotes_api.models import Quote, Reflection


class QuoteSerializer(serializers.ModelSerializer, TaggitSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    tags = TagListSerializerField()

    class Meta:
        model = Quote
        fields = ["id", "user", "text", "author", "tags"]

    # https://stackoverflow.com/questions/21563726/using-django-taggit-with-django-rest-framework-im-not-able-to-save-my-tags
    def create(self, validated_data):
        tags = validated_data.pop("tags")
        instance = super(QuoteSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags")
        instance = super(QuoteSerializer, self).update(instance, validated_data)
        instance.tags.set(*tags)
        return instance


class ReflectionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="owner.username")
    quote = serializers.PrimaryKeyRelatedField(queryset=Quote.objects.all())

    class Meta:
        model = Reflection
        fields = ["id", "user", "quote", "text"]


class UserSerializer(serializers.ModelSerializer):
    quotes = serializers.PrimaryKeyRelatedField(many=True, queryset=Quote.objects.all())
    reflections = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reflection.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "quotes", "reflections"]
