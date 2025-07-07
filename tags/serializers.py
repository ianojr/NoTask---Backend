from rest_framework import serializers
from .models import NoteTags, NoteTasks, Tags, TaskTags

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

        extra_kwargs = {
            'user': {'required' : False}
        }


class NoteTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTags
        fields = '__all__'

class TaskTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTags
        fields = '__all__'

class NoteTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTasks
        fields = '__all__'