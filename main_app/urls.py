from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for plants index
    path('plants/', views.plant_index, name='plant-index'),
    path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
    # new route used to create a plant
    path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),

]