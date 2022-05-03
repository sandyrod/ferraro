from dataclasses import field
from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth.models import Group
#import get_user_model
#AUser = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserByGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'