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

class Plant:
    def __init__(self, name, ailment, description, origin, image):
        self.name = name
        self.ailment = ailment
        self.description = description
        self.origin = origin
        self.image = image



# Create a list of Plant instances
plants = [
    Plant('Manzanilla', 'Stomach Ache', 'Chamomile tea is often used for digestion and calming the stomach.', 'Mexico', 'chamomile.png'),
    # Plant('Eucalipto', 'Cough', 'Eucalyptus leaves are boiled for clearing the lungs and soothing coughs.', 'South America'),
    Plant('Hierba Buena', 'Nausea', 'Mint is steeped into tea to relieve nausea and promote digestion.', 'Mexico', 'mint.png'),
    # Plant('Ruda', 'Menstrual Pain', 'Rue is used traditionally to ease menstrual discomfort.', 'Latin America')
]

def plant_index(request):
    # Render the plants/index.html template with the plants data
    return render(request, 'plants/index.html', {'plants': plants})