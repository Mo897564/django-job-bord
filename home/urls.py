from django.urls import path
from . import views

urlpatterns = [


    path('home/', views.Home_index, name='home_index'),
    
  


]
