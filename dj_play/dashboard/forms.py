from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import CustomUser, Task, Topic, Virtue


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")


class VirtueCreateForm(ModelForm):
    class Meta:
        model = Virtue
        fields = "__all__"


class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
