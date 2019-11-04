from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meals.json', views.index, name='index') #(entry,view function in views.py,name of path to be used elsewhere)
]