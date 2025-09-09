# main_app/views.py

from django.shortcuts import render

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Horse





# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def horse_index(request):
    horses = Horse.objects.all() 
    return render(request, 'horses/index.html', { 'horses': horses })

def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    return render(request, 'horses/detail.html', {'horse': horse})


def home(request):
    return render(request, 'home.html')

# main-app/views.py
class HorseCreate(CreateView):
    model = Horse
    fields = ['name', 'species', 'description', 'age']

class HorseUpdate(UpdateView):
    model = Horse
    # Let's disallow the renaming of aHorse by excluding the name field!
    fields = ['species', 'description', 'age']

class HorseDelete(DeleteView):
    model = Horse
    success_url = '/horses/'


