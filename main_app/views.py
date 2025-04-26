# main_app/views.py
from django.shortcuts import render
from .models import Plant
from django.views.generic.edit import CreateView
from .models import Plant
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
    return render(request, 'plants/detail.html', {'plant': plant})

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




# my db I created is called 'plantcollector2'
#TODO: left at Creating a confirmation template for deleting a cat
# TODO: add image pertaining to the plant in the EDIT page
