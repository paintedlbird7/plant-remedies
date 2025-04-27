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


# Define the home view function
def home(request):
    return render(request, 'home.html')
    
def about(request):
    # return HttpResponse('<h1>About the PlantCollector</h1>')
    return render(request, 'about.html')

def plant_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'plants/detail.html', {
        # include the plant and feeding_form in the context
            'plant': plant, 'feeding_form': feeding_form
        })

class PlantCreate(CreateView):
    model = Plant
    # fields = '__all__'
    fields = ['name', 'ailment', 'description', 'origin', 'image']
    # success_url = '/plants/'

class PlantUpdate(UpdateView):
    model = Plant
    # Let's disallow the renaming of a plant by excluding the name field!
    fields = ['name', 'ailment', 'description', 'origin', 'image']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

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



# my db I created is called 'plantcollector2'
#TODO: left at Adjust the order of feedings
# TODO: add image pertaining to the plant in the EDIT page
