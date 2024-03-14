from django.contrib import admin
from django.urls import include, path

from home import views

urlpatterns = [
   
    path('', views.index,name="index"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('signup/', views.sign_up,name="signup"),
    path('signin/', views.sign_in,name="signin"),
]
