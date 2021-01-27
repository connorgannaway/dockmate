# tickets urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='tickets-home'),
    path('customers/', views.ListCustomers.as_view(), name='list-customers'),
    path('customers/new/', views.CreateCustomer.as_view(), name='create-customer'),
    path('customers/<int:pk>/', views.UpdateCustomer.as_view(), name='update-customer'),
    path('boats/', views.ListBoats.as_view(), name='list-boats'),
    path('boats/new/', views.CreateBoat.as_view(), name='create-boat'),
    path('boats/<int:pk>', views.UpdateBoat.as_view(), name='update-boat'),
    path('tickets/', views.ListTickets, name='list-tickets'),
    path('tickets/new/', views.CreateTicket, name='create-ticket')
]
