import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache.backends.locmem import _caches as cache


# получить комнаты из cache
def rooms_reader():
    rooms = []
    for key in cache['sc']:
        rooms.append(key)
    return rooms


# вызов домашней страницы
def index(request):
    rooms = rooms_reader()
    return render(request, "appchat/index.html", context={'rooms': rooms})


# получить room_name из url
def room(request, room_name):
    room_name = room_name.replace(' ', '_')
    return render(request, "appchat/chatbox.html", context={"room_name": room_name})


# обновить комнаты из cache для index.html
def rooms_return(request):
    rooms = rooms_reader()
    jsn = json.dumps(rooms)
    return HttpResponse(jsn)
