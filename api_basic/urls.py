from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet



urlpatterns = [
    path('', views.article_list),
    path('generic/<int:id>/', views.GenericAPIView.as_view()),
    path('generic/', views.GenericAPIView.as_view()),

]