from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .serializers import crudSerializer
from .models import crud

@api_view(['GET','POST'])
def crud_list(request):
    if request.method == 'GET':
        snippets = crud.objects.all()
        serializer = crudSerializer(snippets, many=True)
        serializer_class = crudSerializer
        permission_classes = [IsAuthenticated]
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = crudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def crud_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = crud.objects.get(id=id)
    except crud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = crudSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = crudSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
