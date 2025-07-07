from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all'

        extra_kwargs = {
            'user': {'required': False}
        }