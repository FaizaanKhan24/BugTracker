from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' 'username' 'email' 'first_name' 'last_name') 

class BugReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugDetails
        fields = '__all__'

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineers
        fields = '__all__'