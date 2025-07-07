from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from tags.models import NoteTags, NoteTasks, Tags, TaskTags
from tags.serializers import NoteTagsSerializer, NoteTasksSerializer, TagsSerializer, TaskTagsSerializer



# tags
@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def Tags_Api(request, id=None):
    if request.method == "GET":
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Optional user linking
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            tag = Tags.objects.get(id=id)
        except Tags.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TagsSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            tag = Tags.objects.get(id=id)
            tag.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Tags.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)


# Notetags
@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def NoteTags_Api(request, id=None):
    if request.method == "GET":
        note_tags = NoteTags.objects.all()
        serializer = NoteTagsSerializer(note_tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NoteTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            note_tag = NoteTags.objects.get(id=id)
        except NoteTags.DoesNotExist:
            return Response({"error": "NoteTag not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteTagsSerializer(note_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            note_tag = NoteTags.objects.get(id=id)
            note_tag.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except NoteTags.DoesNotExist:
            return Response({"error": "NoteTag not found"}, status=status.HTTP_404_NOT_FOUND)


# task Tags
@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def TaskTags_Api(request, id=None):
    if request.method == "GET":
        task_tags = TaskTags.objects.all()
        serializer = TaskTagsSerializer(task_tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            task_tag = TaskTags.objects.get(id=id)
        except TaskTags.DoesNotExist:
            return Response({"error": "TaskTag not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskTagsSerializer(task_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            task_tag = TaskTags.objects.get(id=id)
            task_tag.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except TaskTags.DoesNotExist:
            return Response({"error": "TaskTag not found"}, status=status.HTTP_404_NOT_FOUND)


# Note tasks
@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def NoteTasks_Api(request, id=None):
    if request.method == "GET":
        note_tasks = NoteTasks.objects.all()
        serializer = NoteTasksSerializer(note_tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NoteTasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            note_task = NoteTasks.objects.get(id=id)
        except NoteTasks.DoesNotExist:
            return Response({"error": "NoteTask not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteTasksSerializer(note_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            note_task = NoteTasks.objects.get(id=id)
            note_task.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except NoteTasks.DoesNotExist:
            return Response({"error": "NoteTask not found"}, status=status.HTTP_404_NOT_FOUND)
