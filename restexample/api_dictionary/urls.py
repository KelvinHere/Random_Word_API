from django.urls import path
from .views import GenericAPIView

urlpatterns = [
    path('generic/word/', GenericAPIView.as_view(), name='GenericAPIView'),
    path('generic/word/<int:id>/', GenericAPIView.as_view(), name='GenericAPIView'),
]