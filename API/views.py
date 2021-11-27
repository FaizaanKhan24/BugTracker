from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.

class UserKindViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserKindSerializer

class BugReportViewSet(viewsets.ModelViewSet):
    queryset = BugDetails.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BugReportSerializer

class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EngineerSerializer