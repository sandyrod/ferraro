from dataclasses import field
from rest_framework import serializers
from apps.clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')