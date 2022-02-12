from rest_framework import serializers
from .models import Word

class WordSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)
    meaning = serializers.CharField(style={'base_template': 'textarea.html'})
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('word', instance.word)
        instance.meaning = validated_data.get('meaning', instance.meaning)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance