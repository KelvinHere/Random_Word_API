from django.urls import path
from .views import WordAPIView, WordRUD

urlpatterns = [
    path('word/', WordAPIView.as_view(), name='WordAPIView'),
    path('wordRUD/<id>/', WordRUD.as_view(), name='WordRUD'),
]