from rest_framework import serializers
from .models import Characters


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = ["name", "char_id", "description"]
