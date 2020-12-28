from django.shortcuts import render
from .models import *
# Create your views here.




def home(request):
    Tickets = []
    t = Ticket.objects.filter(completed=False).order_by('timeDue')
    for i in t:
        #ticket info
        TicketID = i.id
        TimeDue = i.timeDue
        #boat info
        Manufacturer = i.boat.manufacturer
        Model = i.boat.model
        Year = i.boat.year
        Slip = i.boat.slip
        #customer info
        FirstName = i.customer.firstName
        LastName = i.customer.lastName

        Ticketitems = i.ticketitem_set.all()
        

        temp = {
            "ticketID":TicketID,
            "timeDue":TimeDue,
            "boat":{
                "manufacturer":Manufacturer,
                "model":Model,
                "year":Year,
                "slip":Slip,
            },
            "customer":{
                "firstName":FirstName,
                "lastName":LastName
            },
            "ticketItems":Ticketitems
        }
        Tickets.append(temp)
    
    
    context = {
        'tickets': Tickets,
        'title':'Home'
    }
    return  render(request, 'tickets/home.html', context)