from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.PositiveIntegerField(default=0)
    dateAdded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Boat(models.Model):
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    slip = models.CharField(max_length=5)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.slip

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    timeCreated = models.DateTimeField(default=timezone.now)
    timeDue = models.DateTimeField()
    completed = models.BooleanField()

    #def __str__(self):
        #return self.customer

class TicketItem(models.Model):
    item = models.CharField(max_length=25)
    description = models.TextField(blank="true")
    completed = models.BooleanField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.item