from rest_framework import serializers

from quotes_app.models import Quote

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author']
