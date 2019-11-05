from django.db import models
import time
import datetime

class Food(models.Model):
    food_name = models.CharField (max_length = 200)
    food_desc = models.TextField(max_length = 1000,default='a PyFood Delicacy')
    cost = models.DecimalField(max_digits = 4, decimal_places =2)
    def __str__(self):
        return self.food_name

class Beverage(models.Model):
    bev_name = models.CharField(max_length = 100)
    bev_desc = models.TextField(max_length = 1000,default='a PyFood Delicacy')
    cost = models.DecimalField(max_digits = 4, decimal_places =2)
    def __str__(self):
        return self.bev_name

class Meal(models.Model):
    x = datetime.datetime.now()
    meal_owner = models.CharField(max_length=100, default = 'a Pyfood customer:'+ x.isoformat())
    pub_date = models.DateTimeField('date published' ,default = x.isoformat() )
    total_cost = models.DecimalField(max_digits = 4, decimal_places =2, default= 3.00)
    feedback = models.TextField(max_length = 1000, default='average')
    food_choice = models.ForeignKey(Food, on_delete=models.CASCADE, default =1)
    drink_choice = models.ForeignKey(Beverage, on_delete=models.CASCADE, default =1)
    # return (self.food_choice) + (self.drink_choice)
    def __str__(self):
        return self.meal_owner

    def mealdateandtime (self):
        return x.isoformat()
