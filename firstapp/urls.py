from django.urls import path
from . import views


urlpatterns = [
    path('v1/',views.view1),
    path('v2/',views.view2),
    path('hv/', views.homeView),
    path('av/', views.aboutView),
    path('cv/', views.contentView),
    path('as/', views.allStudents),
]
