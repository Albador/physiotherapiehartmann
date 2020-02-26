from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "website/home.html"


class ImpressumView(TemplateView):
    template_name = "website/impressum.html"


class LeistungView(TemplateView):
    template_name = "website/leistung.html"


class PraxisView(TemplateView):
    template_name = "website/praxis.html"


class TeamView(TemplateView):
    template_name = "website/team.html"


class OpenView(TemplateView):
    template_name = "website/open.html"
