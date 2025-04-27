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
     # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Define a method to get the URL for this particular plant instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this plant's details
        return reverse('plant-detail', kwargs={'plant_id': self.id})
    
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
       # Create a cat_id column for each feeding in the database
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
