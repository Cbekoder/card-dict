from django.urls import path

from .views import DictionaryListCreateAPIView, redirect_to_docs, DictionaryRetrieveUpdateDestroyAPIView, \
    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, BookRetrieveBySlugAPIView

urlpatterns = [
    path('', redirect_to_docs),
    path('dictionaries/', DictionaryListCreateAPIView.as_view(), name='dictionary-list-create'),
    path('dictionaries/<int:pk>/', DictionaryRetrieveUpdateDestroyAPIView.as_view(), name='dictionary-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('books/<slug:slug>/', BookRetrieveBySlugAPIView.as_view(), name='book-detail-by-slug'),
]