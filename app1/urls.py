from django.contrib import admin
from django.urls import path,include
from app1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home , name="home"),

    path("login", views.login , name="login"),
    path("login1st", views.login1st , name="login1st"),

    path("logout", views.logout , name="logout"),
    path("register", views.register , name="register"),
    path("vmail", views.vmail , name="vmail"),
    path("fvmail", views.fvmail , name="fvmail"),



    
    path("profile_home", views.profile_home , name="profile_home"),
    path("my_profile", views.my_profile , name="my_profile"), 
    path("save_details", views.save_details , name="save_details"), 
    path("save_gallery", views.save_gallery , name="save_gallery"),         
    path("delete_gallery/<int:id>", views.delete_gallery , name="delete_gallery"),  
    path("save_doc", views.save_doc , name="save_doc"),

      
    
    



    path("all_profiles", views.all_profiles , name="all_profiles"),
    path("show_profile/<int:id>", views.show_profile , name="show_profile"),
    
    path("message", views.message , name="message"),
    
    
    path("plans", views.plans , name="plans"),
    
    path("search",views.search, name="search"),
    
    path("follow/<int:uto>",views.follow, name="follow"),
    path("unfollow/<int:uto>",views.unfollow, name="unfollow"),
    
    
    path("follow_accept/<int:id>",views.follow_accept, name="follow_accept"),
    path("follow_reject/<int:id>",views.follow_reject, name="follow_reject"),
    
    
    
    path("notifications",views.notifications, name="notifications"),
    
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 