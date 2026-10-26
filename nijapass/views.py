from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    context = {
        'tourism': [
            {'name':'Zuma Rock, Abuja','img':'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600','desc':'The Gateway to Abuja - 725m monolith'},
            {'name':'Obudu Cattle Ranch','img':'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600','desc':'Clouds & mountains in Cross River'},
            {'name':'Yankari National Park','img':'https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600','desc':'Wildlife safari & warm springs'},
            {'name':'Lekki Conservation Centre','img':'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600','desc':'Longest canopy walkway in Africa'},
        ],
        'hotels': [
            {'id':1,'name':'Transcorp Hilton Abuja','city':'Abuja','price':185000,'img':'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600','rating':'5★ 4.8'},
            {'id':2,'name':'Eko Hotels & Suites','city':'Lagos','price':210000,'img':'https://images.unsplash.com/photo-1551882547-b79c5d92bdf0?w=600','rating':'5★ 4.7'},
            {'id':3,'name':'Obudu Mountain Resort','city':'Calabar','price':95000,'img':'https://images.unsplash.com/photo-1582719478250-c89ca438d85b?w=600','rating':'4★ 4.9'},
        ],
        'cars': [
            {'id':1,'name':'Toyota Prado 2024','type':'SUV - With Driver','price':85000,'img':'https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=600'},
            {'id':2,'name':'Mercedes G-Wagon','type':'Luxury VIP','price':250000,'img':'https://images.unsplash.com/photo-1520050206274-a1ae44613e6d?w=600'},
            {'id':3,'name':'Toyota Coaster Bus','type':'30 Seater - Group','price':120000,'img':'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=600'},
        ],
        'restaurants': [
            {'id':1,'name':'NOK by Alara, Lagos','city':'Fine Dining','price':15000,'img':'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600'},
            {'id':2,'name':'JeVinik, Abuja','city':'Nigerian & Continental','price':8000,'img':'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600'},
            {'id':3,'name':'Yellow Chilli, Lagos','city':'Afro-fusion','price':12000,'img':'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600'},
        ]
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def book_service(request, type, id):
    return render(request, 'booking_success.html', {'type':type,'id':id})

def pay_wallet(request):
    return render(request, 'booking_success.html', {'type':'wallet'})