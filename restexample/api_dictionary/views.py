from random import choice
from urllib import response
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Word
from .serializers import WordSerializer


def home(request):
    return HttpResponse("<b>Random Word Home Page<b> <br><br> Ask for a random word with /word")


class RandomWord(APIView):
    ''' Get Random Word '''
    def get(self, request):
        pks = Word.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        random_word = Word.objects.get(pk=random_pk)
        serializer = WordSerializer(random_word)
        return Response(serializer.data)


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    ''' Retrieve / Update / Destroy word (only'''
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'id'