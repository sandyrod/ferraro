from rest_framework import serializers
from apps.variables.models import Variable

class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = '__all__'