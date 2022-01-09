from django.shortcuts import render

def chat(request):
    return render(request, 'chat.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })