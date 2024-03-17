from django.contrib import admin
from django.urls import include, path

from home import views

urlpatterns = [
   
    path('', views.index,name="index"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('postblog/', views.post_blog,name="postblog"),
    path('signup/', views.sign_up,name="signup"),
    path('signin/', views.sign_in,name="signin"),
    path('logout/', views.log_out,name="logout"),
    path('detail/<int:id>', views.detail,name="detail"),
    path('delete/<int:id>', views.delete_data , name="deletedata"),
    path('edit/<int:id>', views.edit_data , name="editdata"),
    path('editprofile/<int:id>', views.editprofile , name="editprofile"),
]
