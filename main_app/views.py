# main_app/views.py
from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


# Define the home view function
def home(request):
    return render(request, 'home.html')
    
def about(request):
    # return HttpResponse('<h1>About the PlantCollector</h1>')
    return render(request, 'about.html')