# main_app/views.py
from django.shortcuts import render
from .models import Plant

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


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


# my db I created is called 'plantcollector2'