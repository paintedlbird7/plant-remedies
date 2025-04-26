from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    ailment = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    origin = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
