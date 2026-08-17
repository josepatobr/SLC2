from django.urls import path
from . import main

urlpatterns = [
    path('dashboard/', main.dashboard, name=("dashboard")),
]
