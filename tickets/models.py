from os import device_encoding, truncate
from django.db import DefaultConnectionProxy, models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Company

#Model classes are tables objects in a database.
#each variable is a column and its datatype.
#__str__ method defines the name of a object (row) in a database table

class Customer(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.PositiveIntegerField(default=0)
    dateAdded = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Boat(models.Model):
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    slip = models.CharField(max_length=5)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.slip

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    timeCreated = models.DateTimeField(default=timezone.now)
    timeDue = models.DateTimeField()
    completed = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} - {self.customer.firstName} {self.customer.lastName}"

class TicketItem(models.Model):
    item = models.CharField(max_length=25)
    description = models.TextField(blank="true")
    completed = models.BooleanField(default=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item}"