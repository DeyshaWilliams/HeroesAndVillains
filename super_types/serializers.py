from rest_framework import serializers

from .models import Super_types

class Super_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super_types
        fields = ['type', '']