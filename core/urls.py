
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('master/', views.master_function, name='master')
    
]
