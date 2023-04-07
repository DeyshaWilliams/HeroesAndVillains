from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Super_type_Serializer
from .models import Super_type
# Create your views here.

@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        super_types = Super_type.objects.all()
        serializer = Super_type_Serializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Super_type_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
    super_types = get_object_or_404(super_types, pk=pk)
    if request.method == 'GET':
        serializer = Super_type_Serializer(super_types)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Super_type_Serializer(super_types, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
