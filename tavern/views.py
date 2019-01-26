from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Lunch
from .models import Location

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        available_lunches = Lunch.objects.all()

        context = {
            "lunches" : available_lunches
        }

        return context


class Details(TemplateView):
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        available_locations = Location.objects.all()

        context = {
            "location" : available_locations
        }

        return context


class Results(TemplateView):
    template_name = "results.html"

    # def get_context_data(self, **kwargs):







class Vote(TemplateView):
    template_name = "vote.html"

    #
    # def get_context_data(self, **kwargs):
    #     daily_creams = IceCream.objects.filter(available='Daily')
    #     weekly_creams = IceCream.objects.filter(available='Weekly')
    #     seasonal_creams = IceCream.objects.filter(available='Seasonal')
    #     featured_creams = IceCream.objects.filter(featured=True)
    #
    #     context = {
    #         'daily': daily_creams,
    #         'weekly': weekly_creams,
    #         'seasonal': seasonal_creams,
    #         'featured': featured_creams,
    #     }
    #
    #     return context