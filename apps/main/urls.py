from django.urls import path

from .views import DictionaryListCreateAPIView

urlpatterns = [
    path('dictionaries/', DictionaryListCreateAPIView.as_view(), name='dictionary-list-create'),
]