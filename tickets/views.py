from django.shortcuts import render
from extra_views.advanced import InlineFormSet
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin as LRM



# VIEWS

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

@login_required
def ListTickets(request):
    context = {
        'current': getCurrentTickets(),
        'complete': getCompleteTickets(),
        'title': 'Tickets'
    }
    return render(request, 'tickets/ticket_list.html', context)

@login_required
def CreateTicket(request):
    ticketform = TicketForm(instance=Ticket())
    itemform = TicketItemForm(instance=TicketItem())

    context = {
        'ticketform' : ticketform,
        'itemform' : itemform,
        'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
        'title' : 'Ticket Creation'
    }

    return render(request, 'tickets/ticket_form.html', context)

class CreateCustomer(LRM, CreateView):
    model = Customer
    fields = ['firstName', 'lastName', 'email', 'phone']
    
    def get_success_url(self):
        return reverse('list-customers')

class UpdateCustomer(LRM, UpdateView):
    model = Customer
    fields = ['firstName', 'lastName', 'email', 'phone', 'active']
    
    def get_success_url(self):
        return reverse('list-customers')

class ListCustomers(LRM, ListView):
    model = Customer
    context_object_name ='customers'
    ordering = ['-active','lastName']

class CreateBoat(LRM, CreateView):
    model = Boat
    fields = ['manufacturer', 'model', 'year', 'slip', 'owner']

    def get_success_url(self):
        return reverse('list-boats')

class UpdateBoat(LRM, UpdateView):
    model = Boat
    fields = ['manufacturer', 'model', 'year', 'slip', 'owner', 'active']

    def get_success_url(self):
        return reverse('list-boats')

class ListBoats(LRM, ListView):
    model = Boat
    context_object_name = 'boats'
    ordering = ['-active','slip']


# SUPPLEMENTAL

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

def getCompleteTickets():
    Tickets = []
    t = Ticket.objects.filter(completed=True).order_by('-timeDue')
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
