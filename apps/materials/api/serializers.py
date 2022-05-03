from rest_framework import serializers
from apps.materials.models import Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'