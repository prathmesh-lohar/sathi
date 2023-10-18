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



    path("profile", views.profile , name="profile"),
    path("profile_home", views.profile_home , name="profile_home"),
    path("save_personal_detail", views.save_personal_detail , name="save_personal_detail"),

    path("family_details", views.family_details , name="family_details"),

    path("cdp", views.cdp , name="cdp"),
    path("all_profiles", views.all_profiles , name="all_profiles"),
    path("show_profile/<int:id>", views.show_profile , name="show_profile"),


    path("change_profile", views.change_profile , name="change_profile"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 