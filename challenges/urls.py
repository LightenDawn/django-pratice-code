from django.urls import path
from . import views


urlpatterns = [
    path("january", views.january), # first argument = path, second argument = pointer to views.py index function
    path("february", views.february)
]
