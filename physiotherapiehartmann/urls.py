"""
URL configuration for physiotherapiehartmann project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='website:home', permanent=True), name='index'),
    path('website/', include('website.urls')),
    path('admin/', admin.site.urls),
]
