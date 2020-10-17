from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Quote, Reflection


class QuoteCreateForm(ModelForm):
    class Meta:
        model = Quote
        fields = (
            "text",
            "author",
            "tags",
        )
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('user')
        super(QuoteCreateForm, self).__init__(*args, **kwargs)


class ReflectionCreateForm(ModelForm):
    class Meta:
        model = Reflection
        fields = ("text",)
        # fields = '__all__'
