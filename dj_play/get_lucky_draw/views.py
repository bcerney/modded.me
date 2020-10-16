from random import choices

from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import ActionBodyPartCard, StripGameCard


class HomeView(TemplateView):
    template_name = "get_lucky_draw/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["card"] = self.draw_card()
        return context

    def draw_card(self):
        CARD_TYPES = [ActionBodyPartCard, StripGameCard]
        CARD_WEIGHTS = [0.80, 0.20]
        return choices(population=CARD_TYPES, weights=CARD_WEIGHTS, k=1)[0]
