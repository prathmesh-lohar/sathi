from django.contrib import admin
from django.urls import path,include
from dashboard import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", views.dashboard , name="dashboard"),
    path("login", views.login , name="login"),
    path("logout", views.logout , name="logout"),
    
    path("staff/<str:username>/profiles", views.staff , name="staff"),
    
    path("all_staff", views.all_staff , name="all_staff"),
    path("all_profiles", views.all_profiles , name="all_profiles"),
    
    path("reginal_manager", views.reginal_manager , name="reginal_manager"),
    path("reginal_manager/<str:username>/officers", views.staff_unser_reginal_manager , name="staff_unser_reginal_manager"),
    
    
    path("alter_user/<str:username>", views.alter_user , name="alter_user"),
    path("alter_user_save/<str:username>", views.alter_user_save , name="alter_user_save"),
    path("upload_dp/<str:username>", views.upload_dp , name="upload_dp"),
    path("approve_profile/<str:username>", views.approve_profile , name="approve_profile"),
    path("delete_profile/<str:username>", views.delete_profile , name="delete_profile"),
    path("alter_user_family/<str:username>", views.alter_user_family , name="alter_user_family"),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 