from random import choice

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from quotes_app.models import Quote

from .forms import CustomUserCreationForm
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

    def get_context_data(self, **kwargs):
        context = super(VirtueDetailView, self).get_context_data(**kwargs)
        return context
