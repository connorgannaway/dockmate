from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.forms import formset_factory
from django.contrib import messages



# VIEWS

#main view that displays unfinished tickets.
@login_required
def home(request):
    context = {
        'tickets': getTickets(completed=False),
        'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
        'title':'Home'
    }
    return  render(request, 'tickets/home.html', context)

#displays view with no information for non-logged-in users
def base(request):
    return render(request, 'tickets/base.html')

#view that lists finished and unfinished tickets.
@login_required
def ListTickets(request):
    context = {
        'current': getTickets(completed=False),
        'complete': getTickets(completed=True),
        'title': 'Tickets'
    }
    return render(request, 'tickets/ticket_list.html', context)

#view for creating tickets
class CreateTicket(LRM, View):
    template_name = 'tickets/ticket_form.html'
    itemFormset = formset_factory(TicketItemForm) #formset factory handles multiple instances of forms

    #displays blank forms
    def get(self, request, *args, **kwargs):
        context = {
            'ticketform' : TicketForm(instance=Ticket()),
            'itemforms' : self.itemFormset(),
            'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
        }

        return render(request, self.template_name, context)

    #takes form data, validates, and saves
    def post(self, request, *args, **kwargs):
        #copying data to add ForeignKey relationships
        data = self.request.POST.copy()
        nextTicketID = Ticket.objects.all().count() + 1
        nextTicket = True
        formcount = 0
        #looping through forms in post to add foreignkey field
        while nextTicket:
            if data.get(f'form-{formcount}-item'):
                data.appendlist(f'form-{formcount}-ticket', f'{nextTicketID}')
                formcount += 1
            else:
                nextTicket = False
        self.request.POST = data
        #creating form objects from POST data and validating
        itemFormset = self.itemFormset(self.request.POST)
        ticketform = TicketForm(self.request.POST)
        if ticketform.is_valid() and itemFormset.is_valid():
            ticketform.cleaned_data['company'] = self.request.user.profile.company   #not working
            ticketform.save()
            self.createTicketItem(self.request, formcount)
            return HttpResponseRedirect(reverse("list-tickets"))
        
        #if forms aren't valid displays page like 'get' request 
        else:
            messages.error(self.request, "Error creating ticket... (Maybe check the date field?)")
            context = {
            'ticketform' : TicketForm(instance=Ticket()),
            'itemforms' : self.itemFormset(),
            'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
        }
        return render(request, self.template_name, context)

    #creates and saves ticketitem objects in the database
    #from the form info in the POST request.
    def createTicketItem(self, request, formcount):
        for i in range(formcount):
            item = TicketItem(
                item=self.request.POST.get(f'form-{i}-item'),
                description=self.request.POST.get(f'form-{i}-description'),
                ticket=Ticket.objects.last()
                )
            item.save()
            
#single-ticket view that also displays completion form
class ViewTicket(LRM, View):
    template_name = 'tickets/ticket_view.html'
    
    #generate form and pass data
    def get(self, request, pk, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk=pk)

        context = {
            'ticket' : ticket,
            'items' : ticket.ticketitem_set.all(),
            'form' : TicketCompletionForm(instance=ticket),
            'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
            'title' : f'Ticket no.{ticket.id}'
        }
        return render(request, self.template_name, context)

    #save form and generate new form
    def post(self, request, pk, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk=pk)
        form = TicketCompletionForm(self.request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Ticket updated.')
            context = {
            'ticket' : ticket,
            'items' : ticket.ticketitem_set.all(),
            'form' : TicketCompletionForm(instance=ticket),
            'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
            'title' : f'Ticket no.{ticket.id}'
        }
            return render(self.request, self.template_name, context)
        else:
            messages.error(self.request, 'Failure updating ticket.')
            context = {
            'ticket' : ticket,
            'items' : ticket.ticketitem_set.all(),
            'form' : TicketCompletionForm(instance=ticket),
            'currentUsers': getUsernamesFromIDs(getCurrentUsers()),
            'title' : f'Ticket no.{ticket.id}'
        }
            return render(self.request, self.template_name, context)

        

#view for creating customers
class CreateCustomer(LRM, CreateView):
    model = Customer
    fields = ['firstName', 'lastName', 'email', 'phone']
    
    def get_success_url(self):
        return reverse('list-customers')

#view that displays pre-filled form for updating customers
class UpdateCustomer(LRM, UpdateView):
    model = Customer
    fields = ['firstName', 'lastName', 'email', 'phone', 'active']
    
    def get_success_url(self):
        return reverse('list-customers')

#view that lists all customers in database
class ListCustomers(LRM, ListView):
    model = Customer
    context_object_name ='customers'
    ordering = ['-active','lastName']

#view for creating new boats
class CreateBoat(LRM, CreateView):
    model = Boat
    fields = ['manufacturer', 'model', 'year', 'slip', 'owner']

    def get_success_url(self):
        return reverse('list-boats')

#view that displays prefilled form for updating boats
class UpdateBoat(LRM, UpdateView):
    model = Boat
    fields = ['manufacturer', 'model', 'year', 'slip', 'owner', 'active']

    def get_success_url(self):
        return reverse('list-boats')

#View that lists all boat objects in the database
class ListBoats(LRM, ListView):
    model = Boat
    context_object_name = 'boats'
    ordering = ['-active','slip']


# SUPPLEMENTAL

#returns queryset of the currently logged in users
def getCurrentUsers():
    userIds = []
    current_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    for i in current_sessions:
        id = i.get_decoded().get('_auth_user_id', None)
        userIds.append(id)
    return User.objects.filter(id__in=userIds)

#given a queryset of users, pulls and returns the username
def getUsernamesFromIDs(queryset):
    names = []
    for i in queryset:
        name = i.username
        names.append(name)
    return names

#pulls tickets from database based on completion
#formats as and returns a list of dicts
def getTickets(completed):
    Tickets = []
    if completed==True:
        t = Ticket.objects.filter(completed=True).order_by('-timeDue')
    else:
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
