from django.contrib import admin

from main_app.models import Feeding, Plant

admin.site.register(Plant)
# Register the new Feeding model
admin.site.register(Feeding)
