from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Word
from .serializers import WordSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
def word_list(request):
    ''' View to retrieve everything & creating a new word '''
    if request.method == 'GET':
        word = Word.objects.all()
        serializer = WordSerializer(word, many=True)
        return Response(serializer.data)

    # Create word
    if request.method == 'POST':
        serializer = WordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def word_detail(request, pk=None):
    ''' View for Get / Update / Delete operations on words '''
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    # Get word
    if request.method == "GET":
        serializer = WordSerializer(word)
        return Response(serializer.data)

    # Update Word
    if request.method == "PUT":
        serializer = WordSerializer(word, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete Word
    if request.method == "DELETE":
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)