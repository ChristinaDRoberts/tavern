from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Lunch
from .models import Location

class Home(TemplateView):
    template_name = 'home.html'



class Details(TemplateView):
    template_name = "details.html"



class Results(TemplateView):
    template_name = "results.html"



class Vote(TemplateView):
    template_name = "vote.html"
