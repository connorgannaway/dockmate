from django import forms
from . import widgets
from .models import Ticket, TicketItem

#Creating html forms.
# Each class interacts with a model. Fields for a form are chosen in 'fields'
class TicketForm(forms.ModelForm):
    #setting timeDue to have specific formatting
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

