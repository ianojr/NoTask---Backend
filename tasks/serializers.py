from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

        extra_kwargs = {
            'user': {'required' : False}
        }