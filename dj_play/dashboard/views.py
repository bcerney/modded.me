from random import choice

from django.urls import reverse_lazy
from django.views import generic

from quotes_app.models import Quote

from .forms import CustomUserCreationForm


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

        try:
            quote = choice(Quote.objects.filter(user=self.request.user))
        except IndexError:
            quote = None
        context["quote"] = quote

        return context
