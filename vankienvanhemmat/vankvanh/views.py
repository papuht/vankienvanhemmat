from django.shortcuts import render
from .models import Update
from .serializers import UpdateSerializer
from rest_framework import generics





class UpdateListCreate(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

# Create your views here.
