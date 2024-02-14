from django.contrib import admin
from django.urls import path,include
from staff import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.dashboard , name="dashboard"),
    path("login", views.login , name="login"),
    path("logout", views.logout , name="logout"),
    path("add_user", views.add_user , name="add_user"),
    path("alter_user/<str:username>", views.alter_user , name="alter_user"),
    path("delete_user/<str:username>", views.delete_user , name="delete_user"),


    
    path("upload_details/<str:username>", views.upload_details , name="upload_details"),
    path("upload_media/<str:username>", views.upload_media , name="upload_media"),
    path("upload_documents/<str:username>", views.upload_documents , name="upload_documents"),

    path("save_details", views.save_details , name="save_details"),
    path("save_gallery/<str:username>", views.save_gallery , name="save_gallery"),
    path("delete_gallery/<int:id>", views.delete_gallery , name="delete_gallery"),
    


    path("new_profile", views.new_profile , name="new_profile")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 