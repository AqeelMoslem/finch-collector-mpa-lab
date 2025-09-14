# main_app/views.py

from django.shortcuts import render, redirect

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Horse , Toy
from .forms import FeedingForm

from django.views.generic import ListView, DetailView # add these 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
# Other view functions above








@login_required
def horse_index(request):
    horses = Horse.objects.filter(user=request.user)
    return render(request, 'horses/index.html', { 'horses': horses })


# Define the home view function
def home(request):
    return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)

    # Only get the toys the cat does not have
    toys_horse_doesnt_have = Toy.objects.exclude(id__in = horse.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    return render(request, 'horses/detail.html', {
        'horse': horse,
        'feeding_form': feeding_form,
        'toys': toys_horse_doesnt_have  # send those toys
    })


# main-app/views.py
class HorseCreate(LoginRequiredMixin,CreateView):
    model = Horse
    fields = ['name', 'species', 'description', 'age']
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class HorseUpdate(UpdateView):
    model = Horse
    # Let's disallow the renaming of aHorse by excluding the name field!
    fields = ['species', 'description', 'age']

class HorseDelete(DeleteView):
    model = Horse
    success_url = '/horses/'

@login_required
def add_feeding(request, horse_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('horse-detail', horse_id=horse_id)

# Other view functions above

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

@login_required
def associate_toy(request, horse_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Horse.objects.get(id=horse_id).toys.add(toy_id)
    return redirect('horse-detail', horse_id=horse_id)

@login_required
def remove_toy(request, horse_id, toy_id):
    Horse.objects.get(id=horse_id).toys.remove(toy_id)
    return redirect('horse-detail', horse_id=horse_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('horse-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
  
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home') 