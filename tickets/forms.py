from django import forms
from django.forms import widgets
from .models import Ticket, TicketItem

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ["customer", "boat", "timeDue", "completed"]

class TicketItemForm(forms.ModelForm):
    
    class Meta:
        model = TicketItem
        fields = ["item", "description", "completed"]

