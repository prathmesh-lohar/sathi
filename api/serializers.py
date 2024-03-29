from dataclasses import field
from statistics import mode
from rest_framework import serializers

from app1.models import profile
from app1.models import family_details
from app1.models import media
from app1.models import gallery
from app1.models import document
from app1.models import follow

from django.contrib.auth.models import User



class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"
        
        # exclude = ('password',)




class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        # fields = ['name', 'rollno']
        fields= "__all__"
        # exclude = ('password',)
        
class family_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = family_details
        # fields = ['name', 'rollno']
        fields= "__all__"
        # exclude = ('password',)
        
class dpSerializer(serializers.ModelSerializer):
    class Meta:
        model = media
        # fields = ['name', 'rollno']
        fields= "__all__"
        # exclude = ('password',)
        
        
class gallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = "__all__"


class documentSerializer(serializers.ModelSerializer):
    class Meta:
        model = document
        fields = "__all__"


class followSerializer(serializers.ModelSerializer):
    class Meta:
        model = follow
        fields = "__all__"