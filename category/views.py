from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from category.models import Category
from category.serializers import CategorySerializer



@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def Category_Api(request, id=None):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(Category, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"errors": "Category not found"}, status=status.HTTP_404_NOT_FOUND)