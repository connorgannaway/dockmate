# tickets urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='tickets-home'),
    path('home/', views.home, name='tickets-home')

]
