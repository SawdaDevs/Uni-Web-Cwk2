from django.urls import path
from . import views
# import restaurant from views

urlpatterns = [
    path('',views.index, name='index'), #(,view function in views.py,name of)
    path('meals/', views.meals, name = 'meals'),
]