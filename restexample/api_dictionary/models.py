from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField(max_length=4096)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word