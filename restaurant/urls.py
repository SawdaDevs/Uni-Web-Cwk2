from django.urls import path
from . import views
# import restaurant from views

urlpatterns = [
    path('',views.index, name='index'), #(,view function in views.py,name of)
    path('meals.json', views.view_meals, name = 'list of meals'),
    path('add_meal/',views.add_meal, name= 'add meal')
]