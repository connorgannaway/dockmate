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
        temp = {
            "ticketID":i.id,
            "timeDue":i.timeDue,
            "boat":{
                "manufacturer":i.boat.manufacturer,
                "model":i.boat.model,
                "year":i.boat.year,
                "slip":i.boat.slip,
            },
            "customer":{
                "firstName":i.customer.firstName,
                "lastName":i.customer.lastName
            },
            "ticketItems":i.ticketitem_set.all()
        }
        Tickets.append(temp)
    return Tickets