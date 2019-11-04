from django.contrib import admin
from .models import Meal
from .models import Food
from .models import Beverage

admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Beverage)