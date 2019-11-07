#view functions go here and will be for each of the things I have.
from django.http import HttpResponse, JsonResponse, QueryDict #JsonResponse builds JSON resp object 
from django.shortcuts import render
from django.template import loader #what does this do...?
from .models import Meal, Food, Beverage
from django.views.decorators.csrf import csrf_exempt
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
    return render(request,'restaurant/index.html', {
        'meal': Meal.objects.all()
    })

def meals(request):
    if request.method == 'POST':
        ml = request.POST['meal-owner']
        feedback = request.POST['feedback']
        new_ml = Meal(meal_owner=ml, feedback=feedback)
        new_ml.save()
        return JsonResponse({
        'id': new_ml.id,
        'meal_owner' : new_ml.meal_owner
        })
    if request.method == 'GET':
        return JsonResponse({
        'meals': list(Meal.objects.values()) #list of dictionaries, dictionaries being key values eg name: Sawda. A list of them being like a Json Payload 
        })
def food(request):
    if request.method == 'POST':
        fd = request.POST['food-name']
        desc = request.POST['food-desc']
        cst = request.POST['food-cost']
        new_fd = Food(food_name=fd, food_desc=desc, cost=cst)
        new_fd.save()
        print(new_fd)
        return JsonResponse({
        'id': new_fd.id,
        'food_name' : new_fd.food_name,
        'food_desc' : new_fd.food_desc,
        'food_cost': new_fd.cost
        })
    if request.method == 'GET':
        return JsonResponse({
        'food': list(Food.objects.values()) #list of dictionaries, dictionaries being key values eg name: Sawda. A list of them being like a Json Payload 
        })
def bev(request):
    if request.method == 'POST':
        bv = request.POST['bev-name']
        new_bv =Beverage(bev_name=bv)
        new_bv.save()
        return JsonResponse({
        'id': new_bv.id,
        'bev_name' : new_bev.bev_name
        })
    if request.method == 'GET':
        return JsonResponse({
        'bev': list(Beverage.objects.values()) #list of dictionaries, dictionaries being key values eg name: Sawda. A list of them being like a Json Payload 
        }) 

@csrf_exempt
def meals_change(request):
    if request.method =='PUT':
        id = int(QueryDict(request.body).get('id'))
        new_name = QueryDict(request.body).get('name')
        meal_ch = Meal.objects.get(id = id)
        meal_ch.meal_owner=new_name
        print(meal_ch)
        # meal_ch.name = new_name
        meal_ch.save() 
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response

    if request.method == 'DELETE':
        id = int(QueryDict(request.body).get('id'))
        # print(QueryDict(request.body))
        meal_del = Meal.objects.get(id=id)
        meal_del.delete()
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response

@csrf_exempt
def food_change(request):
    if request.method =='PUT':
        id = int(QueryDict(request.body).get('id'))
        new_name = QueryDict(request.body).get('name')
        fd_ch = Food.objects.get(id = id)
        fd_ch.food_name=new_name
        fd_ch.save() 
        print(fd_ch)
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response
    if request.method == 'DELETE':
        id = int(QueryDict(request.body).get('id'))
        food_del = Food.objects.get(id=id)
        food_del.delete()
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response

@csrf_exempt
def bev_change(request):
    if request.method =='PUT':
        id = int(QueryDict(request.body).get('id'))
        new_name = QueryDict(request.body).get('name')
        bev_ch = Beverage.objects.get(id = id)
        bev_ch.bev_name=new_name
        bev_ch.save() 
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response
    if request.method == 'DELETE':
        id = int(QueryDict(request.body).get('id'))
        bev_del = Beverage.objects.get(id=id)
        bev_del.delete()
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response