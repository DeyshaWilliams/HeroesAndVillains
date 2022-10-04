from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Super_type_Serializer
from .models import Super_types
# Create your views here.

@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        super_types = Super_types.objects.all()
        serializer = Super_type_Serializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Super_type_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
    supers_type = get_object_or_404(Super_types, pk=pk)
    if request.method == 'GET':
        serializer = Super_type_Serializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Super_type_Serializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
