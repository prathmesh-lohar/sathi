from django.contrib import admin
from django.urls import path, include
from django.views import View
from api import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_simplejwt.views import TokenVerifyView


# router = routers.DefaultRouter()
# router.register(r'testing', views.TestingViewSet)

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    
    path('users',views.usersClassBassedView.as_view()),
    path('user/<int:id>',views.usersClassBassedView.as_view()),
    
    path('profile',views.profileClassBassedView.as_view()),
    path('profile/<int:id>',views.profileClassBassedView.as_view()),
    
    path('family_details/<int:id>',views.family_detailsClassBassedView.as_view()),
    
    path('dp/<int:id>',views.dpClassBassedView.as_view()),
    path('gallery/<int:id>',views.galleryClassBassedView.as_view()),
    path('document/<int:id>',views.documentClassBassedView.as_view()),
    path('follow/<int:id>',views.followClassBassedView.as_view()),
    
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 