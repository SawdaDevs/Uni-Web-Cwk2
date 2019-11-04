#configure the urls for the whole site, so site/restuar.. will take to the urls for restuarant etc
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('restaurant/', include('restaurant.urls')),
    path('admin/', admin.site.urls),
]