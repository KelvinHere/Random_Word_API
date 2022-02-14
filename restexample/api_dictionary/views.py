from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Word
from .serializers import WordSerializer


class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'id'