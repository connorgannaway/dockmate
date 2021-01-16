from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'tickets': getCurrentTickets(),
        'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
        'title':'Home'
    }
    return  render(request, 'tickets/home.html', context)

def base(request):
    return render(request, 'tickets/base.html')


def getCurrentUsers():
    userIds = []
    current_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    for i in current_sessions:
        id = i.get_decoded().get('_auth_user_id', None)
        userIds.append(id)
    return User.objects.filter(id__in=userIds)

def getUsernamesFromIDs(queryset):
    names = []
    for i in queryset:
        name = i.username
        names.append(name)
    return names


def getCurrentTickets():
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
    return Tickets