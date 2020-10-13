from django.urls import path
from . import views


urlpatterns = [
    path('ns/', views.newStudent, name='newstudent'),
    path('allstu/',views.allStudents, name='allstudents'),
]