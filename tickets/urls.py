# tickets urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='tickets-home')

]
