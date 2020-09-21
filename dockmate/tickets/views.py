from django.shortcuts import render
# Create your views here.

people = [
    {
        'id':'0001',
        'firstName':'Andrew',
        'lastName':'Parks',
        'email':'mail1@test.com',
        'boat':['0002']
    },
    {
        'id':'0002',
        'firstName':'Jackson',
        'lastName':'Dodd',
        'email':'mail2@test.com',
        'boat':['0001']
    }
]

boats = [
    {
        'id':'0001',
        'manufacturer':'MasterCraft',
        'model':'XT23',
        'slipID':'B12'
    },
    {
        'id':'0002',
        'manufacturer':'Malibu',
        'model':'Wakesetter NXZ',
        'slipID':'A3'
    }
]

tickets = [
    {
        'customerID':'0001',
        'boatID':'0002',
        'gas':True,
        'inWater':True,
        'onRack':False,
        'ice':True,
        'Maintenance':False,
        'time':'10:30'
    },
    {
        'customerID':'0002',
        'boatID':'0001',
        'gas':False,
        'inWater':False,
        'onRack':True,
        'ice':False,
        'Maintenance':'Oil Tique and De-Winterize',
        'time':'10:30'
    }
]


def home(request):
    context = {
        'tickets':tickets,
        'people':people,
        'boats':boats,
        'title':'Home'
    }
    return  render(request, 'tickets/home.html', context)