from django.shortcuts import render

def home(request):
    return render(request, 'chatapp/home.html')

def room(request, room_name):
    return render(request, 'chatapp/room.html', {'room_name': room_name})
