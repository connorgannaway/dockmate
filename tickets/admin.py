from django.contrib import admin
from .models import Customer, Boat, Ticket, TicketItem

#registering models with admin site
admin.site.register(Customer)
admin.site.register(Boat)
admin.site.register(Ticket)
admin.site.register(TicketItem)