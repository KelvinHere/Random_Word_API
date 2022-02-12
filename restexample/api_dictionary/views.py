from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Word
from .serializers import WordSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


class WordAPIView(APIView):
    def get(self, request):
        ''' Retrieve everything & creating a new word '''
        if request.method == 'GET':
            word = Word.objects.all()
            serializer = WordSerializer(word, many=True)
            return Response(serializer.data)

    def post(self, request):
        ''' Create a new word '''
        if request.method == 'POST':
            serializer = WordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordRUD(APIView):
    def get_object(self, id):
        try:
            return Word.objects.get(id=id)
        except Word.DoesNotExist:
            print("##################### EXCEPTION ")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        word = self.get_object(id)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, id):
        word = self.get_object(id)
        serializer = WordSerializer(word, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        word = self.get_object(id)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)