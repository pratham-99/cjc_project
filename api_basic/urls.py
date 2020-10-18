from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('generic/<int:id>/', views.GenericAPIView.as_view()),
    path('generic/', views.GenericAPIView.as_view()),
]