from django.urls import path
from .views import WordList, WordDetail

urlpatterns = [
    path('word/', WordList.as_view()),
    path('word/<int:id>/', WordDetail.as_view()),
]