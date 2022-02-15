from django.urls import path
from .views import RandomWord, WordDetail, home

urlpatterns = [
    path('', home, name='home'),
    path('word/', RandomWord.as_view()),
    path('word/<int:id>/', WordDetail.as_view()),
]