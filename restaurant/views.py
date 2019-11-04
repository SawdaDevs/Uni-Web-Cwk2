#view functions go here and will be for each of the things I have.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader #what does this do...?
from .models import Meal
# def home(request):
#     return render(request, ''){

#     } 
def index(request):
    # latest_meals_list = Meal.objects.order_by('pub_date') #order by meal owner and saves in this array
    # template = loader.get_template('restaurant/index.html')
    # context ={
    #     'meals': latest_meals_list, 
    # }
    # return HttpResponse(template.render(context,request))
    return render(request,'restaurant/index.html',{
        'meals': Meal.objects.all(),
    })
def view_meals(request):
    return JsonResponse({
        'meals': list(Meal.objects.values()) #list of dictionaries
    }
        
    )    