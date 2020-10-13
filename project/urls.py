from django.contrib import admin
from django.urls import path, include
from EcommerceApp.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('fa/',include('firstapp.urls')),
    path('ta/',include('thirdapp.urls')),
    path('sa/',include('secondapp.urls')),
    path('ecomm/',include('EcommerceApp.urls')),
    path('formv/',include('formvalidapp.urls')),

]
