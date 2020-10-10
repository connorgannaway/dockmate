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

#even dummier dummy data
timedTickets = [
    {
        'id':'0001',
        'customer':'Jackson Dodd',
        'boat':{
            'manufacturer':'Mastercraft',
            'model':'XT23',
            'year':'2015',
            'Slip':'B15'
        },
        'timePlaced':'10:30',
        'timeOut':'11:00',
        'date':'July 21, 2020',
        'items': [
            'In Water',
            'Gas',
            'Ice'

        ]
    },
    {
        'id':'0002',
        'customer':'Ethan Morrell',
        'boat':{
            'manufacturer':'Malibu',
            'model':'Wakesetter NXZ',
            'year':'2016',
            'Slip':'A5'
        },
        'timePlaced':'10:30',
        'timeOut':'11:30',
        'date':'July 21, 2020',
        'items': [
            'In Water',
            'Gas',
            'Ice'
            
        ]
    },
    {
        'id':'0003',
        'customer':'Braxton Lazarus',
        'boat':{
            'manufacturer':'Mastercraft',
            'model':'X-Star',
            'year':'2018',
            'Slip':'A28'
        },
        'timePlaced':'11:00',
        'timeOut':'12:00',
        'date':'July 21, 2020',
        'items': [
            'In Water',
            'Gas',
        ]
    }
]



def home(request):
    context = {
        'timedTickets': timedTickets,
        'title':'Home'
    }
    return  render(request, 'tickets/home.html', context)