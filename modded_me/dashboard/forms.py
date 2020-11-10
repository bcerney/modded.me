from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ModelChoiceField

from .models import CustomUser, Task, Topic, Virtue


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")


class VirtueCreateForm(ModelForm):
    class Meta:
        model = Virtue
        fields = ["title", "description"]


class TopicCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(TopicCreateForm, self).__init__(*args, **kwargs)
        self.fields["virtue"] = ModelChoiceField(
            queryset=Virtue.objects.filter(user_profile=user.userprofile)
        )

    class Meta:
        model = Topic
        fields = "__all__"


class TaskCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        virtues = Virtue.objects.filter(user_profile=user.userprofile)
        self.fields["virtue"] = ModelChoiceField(queryset=virtues)
        self.fields["topic"] = ModelChoiceField(
            queryset=Topic.objects.filter(virtue__in=virtues)
        )

    class Meta:
        model = Task
        fields = ["title", "description", "notes", "xp", "virtue", "topic"]
