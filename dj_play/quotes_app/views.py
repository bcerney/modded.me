from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import QuoteCreateForm, ReflectionCreateForm
from .models import Quote, Reflection


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'quotes_app/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['quotes'] = Quote.objects.all()
        context['reflections'] = Reflection.objects.all()
        return context


class QuoteCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'quotes_app/add_quote.html'
    form_class = QuoteCreateForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Quote
    template_name = 'quotes_app/quote_detail.html'


class ReflectionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reflection
    template_name = 'quotes_app/reflection_detail.html'

