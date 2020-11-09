import math
from datetime import datetime
from random import choice

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template.loader import render_to_string

from quotes_app.models import Quote

from .forms import (
    CustomUserCreationForm,
    TaskCreateForm,
    TopicCreateForm,
    VirtueCreateForm,
)
from .models import (
    CustomUser,
    Sprint,
    SprintVirtueTally,
    Task,
    Topic,
    UserProfile,
    Virtue,
)
from .tasks import send_daily_snapshot_email


class IndexView(generic.TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


# TODO: add messages.success on signup
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# https://code.tutsplus.com/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
def verify(request, uuid):
    try:
        user = CustomUser.objects.get(verification_uuid=uuid, is_verified=False)
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist")

    user.is_verified = True
    user.save()
    messages.success(request, f"User {user.username} has been verified")

    return redirect("login")


class DashboardView(generic.TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        user = self.request.user
        user_profile = user.userprofile

        try:
            quote = choice(Quote.objects.filter(user=user))
        except IndexError:
            # TODO: add default quotes from some default quote user
            quote = None
        context["quote"] = quote

        virtues = Virtue.objects.filter(user_profile_id=user_profile.id).all()
        context["virtues"] = virtues

        sprint = Sprint.objects.get(user_profile_id=user_profile.id, is_active=True)
        context["sprint"] = sprint

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


class SprintDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sprint
    template_name = "dashboard/sprint-detail.html"

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        # TODO: add more stats via SprintVirtueTally
        return context


class VirtueDetailView(LoginRequiredMixin, generic.DetailView):
    model = Virtue
    template_name = "dashboard/virtue-detail.html"


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
        sprint = Sprint.objects.get(
            user_profile_id=request.user.userprofile.id, is_active=True
        )
        virtue = task.virtue

        msgs = self.complete_task(task, virtue, sprint)
        for message in msgs:
            messages.success(request, message)

        return redirect("dashboard:dashboard")

    def complete_task(self, task, virtue, sprint):
        msgs = []
        message = virtue.add_task_xp(task)
        virtue.save()
        msgs.append(message)

        # TODO: move to model method
        task.is_active = False
        task.completed = datetime.now()
        task.save()
        msgs.append(
            f"{virtue.user_profile.user.username} gained {task.xp} XP  in {virtue.title} by completing task: {task.title}!"
        )
        # TODO: move to model method
        virtue_tally = SprintVirtueTally.objects.get(virtue=virtue, sprint=sprint)
        virtue_tally.total_xp += task.xp
        virtue_tally.tasks_completed += 1
        virtue_tally.save()

        return msgs


class DailySnapshotView(LoginRequiredMixin, generic.base.View):
    def get(self, request, *args, **kwargs):
        UserModel = get_user_model()
        user = get_object_or_404(UserModel, pk=request.user.id)

        send_daily_snapshot_email.delay(user.id)
        messages.success(
            request, f"Daily Snapshot for User {user.username} has been sent"
        )

        return redirect("dashboard:dashboard")
