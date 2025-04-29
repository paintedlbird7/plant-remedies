from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# A tuple of 2-tuples added above our models
MEALS = (
    ('W', 'Water'),
    ('S', 'Sun'),
    ('F', 'Fertilizer'),
    ('P', 'Pruning'),
    ('H', 'Harvest'),
)


class Plant(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    ailment = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    origin = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Reverse relationship for recipes
    recipes = models.ManyToManyField('Recipe', related_name='plants', blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'plant_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    
# new Feeding model below Plant model
class Feeding(models.Model):
# The first optional positional argument overrides the label
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
       # Create a plant_id column for each feeding in the database
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plant_recipes')


    def __str__(self):
        return f"{self.title} Recipe for {self.plant.name}"
