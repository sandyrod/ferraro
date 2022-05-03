from rest_framework import serializers
from apps.providers.models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class ProviderMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name')