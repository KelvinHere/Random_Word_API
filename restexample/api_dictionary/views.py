from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Word
from .serializers import WordSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def word_list(request):
    ''' View to retrieve everything & creating a new word '''
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Create word
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WordSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def word_detail(request, pk=None):
    ''' View for Get / Update / Delete operations on words '''
    word = get_object_or_404(Word, pk=pk)

    # Get word
    if request.method == "GET":
        serializer = WordSerializer(word)
        return JsonResponse(serializer.data)

    # Update Word
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = WordSerializer(word, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    # Delete Word
    if request.method == "DELETE":
        word.delete()
        return HttpResponse(status=204)