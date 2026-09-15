"""
URL configuration for the website app.

https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.urls import path

from website.views import HomeView, ImpressumView, LeistungView, OpenView, PraxisView, TeamView

app_name = 'website'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('impressum/', ImpressumView.as_view(), name='impressum'),
    path('leistung/', LeistungView.as_view(), name='leistung'),
    path('praxis/', PraxisView.as_view(), name='praxis'),
    path('team/', TeamView.as_view(), name='team'),
    path('open/', OpenView.as_view(), name='open'),
]
