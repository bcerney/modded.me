from datetime import datetime
import math
from random import choice

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from quotes_app.models import Quote

from .forms import (
    CustomUserCreationForm,
    TaskCreateForm,
    TopicCreateForm,
    VirtueCreateForm,
)
from .models import Task, Topic, UserProfile, Virtue


class IndexView(generic.TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class DashboardView(generic.TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        user = self.request.user
        user_profile = user.userprofile

        try:
            quote = choice(Quote.objects.filter(user=user))
        except IndexError:
            quote = None
        context["quote"] = quote

        virtues = Virtue.objects.filter(user_profile_id=user_profile.id).all()
        context["virtues"] = virtues

        # TODO: allow for multi-column rows, deal with odd numbers
        # virtues_rows = []
        # for i in range(0, len(virtues), 2):
        #     row = [
        #         virtues[i],
        #         virtues[i+1],
        #     ]
        #     virtues_rows.append(row)
        # context["virtue_rows"] = virtues_rows

        return context


class VirtueDetailView(LoginRequiredMixin, generic.DetailView):
    model = Virtue
    template_name = "dashboard/virtue-detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super(VirtueDetailView, self).get_context_data(**kwargs)
    #     return context


class VirtueCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = VirtueCreateForm
    template_name = "dashboard/add-virtue.html"

    def get_success_url(self):
        return reverse("dashboard:dashboard")


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    template_name = "dashboard/topic-detail.html"


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TopicCreateForm
    template_name = "dashboard/add-topic.html"

    # def get_success_url(self):
    #     return reverse('dashboard:dashboard')


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "dashboard/task-detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TaskCreateForm
    template_name = "dashboard/add-task.html"

    # def get_success_url(self):
    #     return reverse('dashboard:dashboard')


class CompleteTaskView(LoginRequiredMixin, generic.base.View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        virtue = task.virtue
        self.complete_task(task, virtue)
        return redirect("dashboard:dashboard")

    def complete_task(self, task, virtue):
        virtue.add_task_xp(task)
        virtue.save()

        task.is_active = False
        task.completed = datetime.now()
        task.save()
