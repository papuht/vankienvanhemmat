from django.shortcuts import render
from .models import Update, Backgrounds
from .serializers import UpdateSerializer, BackgroundSerializer
from rest_framework import generics


class UpdateListCreate(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

class BackgroundListCreate(generics.ListCreateAPIView):
    queryset = Backgrounds.objects.all()
    serializer_class = BackgroundSerializer


