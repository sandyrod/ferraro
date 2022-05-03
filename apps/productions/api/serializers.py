from rest_framework import serializers
from apps.productions.models import Production
from apps.clients.api.serializers import ClientMinSerializer
from apps.providers.api.serializers import ProviderMinSerializer

class ProductionSerializer(serializers.ModelSerializer):

    #client = ClientMinSerializer(many=False, read_only=False)
    #provider = ProviderMinSerializer(many=False, read_only=False)

    class Meta:
        model = Production
        fields = '__all__'