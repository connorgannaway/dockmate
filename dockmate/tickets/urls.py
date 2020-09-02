# tickets urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tickets-home')
]
