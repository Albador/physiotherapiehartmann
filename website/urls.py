"""physiotherapiehartmann URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from website.views import HomeView, ImpressumView, LeistungView, PraxisView, TeamView, OpenView

app_name = 'website'

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('impressum', ImpressumView.as_view(), name='impressum'),
    path('leistung', LeistungView.as_view(), name='leistung'),
    path('praxis', PraxisView.as_view(), name='praxis'),
    path('team', TeamView.as_view(), name='team'),
    path('open', OpenView.as_view(), name='open'),
]
