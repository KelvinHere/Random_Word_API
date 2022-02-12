from django.urls import path
from .views import word_detail, word_list

urlpatterns = [
    path('word/', word_list, name='word_list'),
    path('word_detail/<pk>/', word_detail, name='word_detail'),
]