from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from EcommerceApp.views import home
from api_basic.views import ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',home),
    path('fa/',include('firstapp.urls')),
    path('ta/',include('thirdapp.urls')),
    path('sa/',include('secondapp.urls')),
    path('ecomm/',include('EcommerceApp.urls')),
    path('formv/',include('formvalidapp.urls')),
    path('art/', include('api_basic.urls')),
]
