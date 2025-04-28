# main_app/views.py
from django.shortcuts import render
from .models import Plant
from django.views.generic.edit import CreateView
from .models import Plant
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

def home(request):
    form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})

def about(request):
    # return HttpResponse('<h1>About the DogCollector</h1>')
    return render(request, 'about.html')

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    
def about(request):
    # return HttpResponse('<h1>About the PlantCollector</h1>')
    return render(request, 'about.html')

@login_required
def plant_index(request):
    plants = Plant.objects.filter(user=request.user)
    # You could also retrieve the logged in user's plants like this
    # plants = request.user.plants_set.all()
    return render(request, 'cats/index.html', { 'plants': plants })

@login_required
def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'plants/detail.html', {
        # include the plant and feeding_form in the context
            'plant': plant, 'feeding_form': feeding_form
        })

LoginRequiredMixin,
class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'ailment', 'description', 'origin', 'image']

    # This inherited method is called when a
    # valid plant form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the plant
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    # Let's disallow the renaming of a plant by excluding the name field!
    fields = ['name', 'ailment', 'description', 'origin', 'image']

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

@login_required
def add_feeding(request, plant_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the plant_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    return redirect('plant-detail', plant_id=plant_id)

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
            return redirect('plant-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )



# my db I created is called 'plantcollector2'
#TODO: left at Update the PlantCreate view to assign a new plant to the logged in user
# TODO: add image pertaining to the plant in the EDIT page
