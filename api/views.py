from django.shortcuts import render

from api.models import Photo, AlbumAuto, AlbumUser, Face, Person
from rest_framework import viewsets
from api.serializers import PhotoSerializer
from api.serializers import FaceSerializer
from api.serializers import AlbumAutoSerializer
from api.serializers import PersonSerializer
# Create your views here.

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-exif_timestamp')
    serializer_class = PhotoSerializer

class FaceViewSet(viewsets.ModelViewSet):
    queryset = Face.objects.all().order_by('-person')
    serializer_class = FaceSerializer

class AlbumAutoViewSet(viewsets.ModelViewSet):
    queryset = AlbumAuto.objects.all().order_by('-timestamp')
    serializer_class = AlbumAutoSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer