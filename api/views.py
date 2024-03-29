from unicodedata import name
from urllib import response
from urllib.request import Request
from django.shortcuts import render


from api.serializers import profileSerializer
from api.serializers import family_detailsSerializer
from api.serializers import dpSerializer
from api.serializers import gallerySerializer
from api.serializers import documentSerializer
from api.serializers import followSerializer
from api.serializers import usersSerializer


from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from app1.models import profile
from app1.models import family_details
from app1.models import media
from app1.models import gallery
from app1.models import document
from app1.models import follow
from django.contrib.auth.models import User


# Create your views here.


# class TestingViewSet(viewsets.ModelViewSet):

#     queryset = testing.objects.all()
#     serializer_class = testingSerializer

#     # authentication_class = [TokenAuthentication]
#     # permission_class = [IsAuthenticated]



class usersClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = User.objects.get(user_id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = usersSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= User.objects.all()
        s = usersSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = usersSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=User.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = usersSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= User.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)



class family_detailsClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = family_details.objects.get(user_id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = family_detailsSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        # tt= profile.objects.all()
        # s = profileSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = family_detailsSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=family_details.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = family_detailsSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= family_details.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)



class profileClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = profile.objects.get(user_id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = profileSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= profile.objects.all()
        s = profileSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = profileSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=profile.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = profileSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= profile.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)



class dpClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = media.objects.get(user_id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = dpSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= media.objects.all()
        s = dpSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = profileSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=media.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = dpSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= media.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)




class galleryClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = gallery.objects.filter(user_id=id)
                # tt = gallery.objects.all()
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = gallerySerializer(tt,many=True)

            return Response(s.data, status=status.HTTP_200_OK)
        # tt= media.objects.all()
        # s = dpSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = gallerySerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=gallery.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = gallerySerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= gallery.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)
    
    
    
    
    
class documentClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = document.objects.filter(user_id=id)
                # tt = gallery.objects.all()
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = documentSerializer(tt,many=True)

            return Response(s.data, status=status.HTTP_200_OK)
        # tt= media.objects.all()
        # s = dpSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = documentSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=document.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = documentSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= document.objects.get(user_id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)


class followClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = follow.objects.filter(uto=id)
                # tt = gallery.objects.all()
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = followSerializer(tt,many=True)

            return Response(s.data, status=status.HTTP_200_OK)
        # tt= media.objects.all()
        # s = dpSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = followSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=follow.objects.get(uto=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = followSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= follow.objects.get(uto=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)
