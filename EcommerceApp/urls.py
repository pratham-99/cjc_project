from django.urls import path
from . import views

urlpatterns = [
    path('ac/', views.addCustomer, name='addCustomer'),
    path('allc/',views.allCustomer, name='allcustomer'),
    path('adds/',views.addStudent, name='addStudent'),
    path('addc/',views.addCustomerDj, name='addcustomerDJ'),
    path('addo/',views.addOrder, name='addorder'),
    path('allo/',views.allOrder, name='allorder'),
    path('', views.home, name='home'),
    path('delete/<int:oid>/',views.deleteOrder, name='delete'),
    path('update/<int:oid>/', views.updateOrder, name='update'),
    path('reg/',views.registrationView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('contact/', views.contact, name='contact'),
]