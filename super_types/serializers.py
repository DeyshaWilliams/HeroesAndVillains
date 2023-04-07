from rest_framework import serializers

from .models import Super_type

class Super_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super_type
        fields = ['type']