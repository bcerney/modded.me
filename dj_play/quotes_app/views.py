from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from taggit.models import Tag

from .forms import QuoteCreateForm, ReflectionCreateForm
from .models import Quote, Reflection


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "quotes_app/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["quotes"] = Quote.objects.filter(user=self.request.user)
        return context


class QuoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Quote
    template_name = "quotes_app/quote_detail.html"

    def get_context_data(self, **kwargs):
        context = super(QuoteDetailView, self).get_context_data(**kwargs)
        return context


class QuoteCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = QuoteCreateForm
    template_name = "quotes_app/add_quote.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReflectionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reflection
    template_name = "quotes_app/reflection_detail.html"


class ReflectionCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ReflectionCreateForm
    template_name = "quotes_app/add_reflection.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.quote = Quote.objects.get(id=self.kwargs["quote_id"])
        return super().form_valid(form)


class TagQuoteListView(LoginRequiredMixin, generic.TemplateView):
    template_name = "quotes_app/tag_quotes.html"

    def get_context_data(self, **kwargs):
        context = super(TagQuoteListView, self).get_context_data(**kwargs)

        tag = Tag.objects.get(id=context["pk"])
        context["tag"] = tag

        context["quotes"] = Quote.objects.filter(
            # https://django-taggit.readthedocs.io/en/latest/api.html#filtering
            user=self.request.user,
            tags__name__in=[tag.name],
        )
        return context
