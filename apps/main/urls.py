from django.urls import path

from .views import DictionaryListCreateAPIView, redirect_to_docs

urlpatterns = [
    path('', redirect_to_docs),
    path('dictionaries/', DictionaryListCreateAPIView.as_view(), name='dictionary-list-create'),
]