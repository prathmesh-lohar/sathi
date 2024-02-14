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
    
    path("alter_user/<str:username>", views.alter_user , name="alter_user"),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 