from django import forms
from . import widgets
from .models import Ticket, TicketItem

class TicketForm(forms.ModelForm):
    timeDue = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=widgets.DateTimeField()
    )
    class Meta:
        model = Ticket
        fields = ["customer", "boat", "timeDue"]

class TicketItemForm(forms.ModelForm):
    
    class Meta:
        model = TicketItem
        fields = ["item", "description"]

