from django.urls import path
from . import views
# import restaurant from views

urlpatterns = [
    path('',views.index, name='index'), #(,view function in views.py,name of)
    path('meals/', views.meals, name = 'meals'),
    path('food/', views.food, name = 'food'),
    path('bev/', views.bev, name = 'bev'),
    
    path('meals2/',  views.meals_change, name='meals-change'),
    path('food2/',  views.food_change, name='food-change'),
    path('bev2/',  views.bev_change, name='bev-change')
]