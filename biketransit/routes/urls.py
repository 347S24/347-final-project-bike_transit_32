from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.routes, name='routes'),
    path('saved/', views.saved_routes, name='saved_routes'),
]