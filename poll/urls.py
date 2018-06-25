from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern to home page
    path(r'', views.home, name='home'),
    ]
